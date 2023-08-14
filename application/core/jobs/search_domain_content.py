
import requests
import tracemalloc
import asyncio
from bs4 import BeautifulSoup
from application import create_app, db
from application.core.db_models import DomainInfo
from itertools import zip_longest
import re


def search_domain_content(file):
    def __save_content(content_dict):
        domain_info_record = DomainInfo(domain_name=content_dict.get('domain_name'),
                                        status_code=content_dict.get('status_code'),
                                        title=content_dict.get('title'),
                                        content=content_dict.get('content'),
                                        is_it_key=content_dict.get('is_it_key'),
                                        is_active=content_dict.get('is_active'),
                                        extra_info=content_dict.get('extra_info')
                                        )
        db.session.add(domain_info_record)
        db.session.commit()


    def __get_title(content):
        domain_title = None
        try:
            if content.text:
                soup = BeautifulSoup(content.text, "html.parser")
                domain_title = soup.title.text.strip() if soup.title else None
            else:
                pass
        except requests.exceptions.RequestException as e:
            print(e)
            pass
        return domain_title


    def __execute_regex(content):
        pattern = r"(api key|secret key|token|api_key|acces token|api_key)[:=\s]*([\'\"]?[\w\d]+[\'\"]?)"
        dict_item = {}
        tuple_regex = re.findall(pattern, content, re.IGNORECASE)
        if len(tuple_regex) == 1:
            for i in tuple_regex:
                dict_item["secret_key"] = i[0] + "=" + i[1]
        elif len(tuple_regex) == 0:
            return dict_item
        else:
            dict_list = []
            for i in tuple_regex:
                dict_list.append(i[0] + "=" + i[1])
            dict_item["secret_key"] = dict_list
        if dict_item:
            pass
        else:
            pass
        return dict_item

    async def main():
        processed_line_count = 0
        with open(file_path, "r", encoding="utf-8") as f:
            for next_n_lines in zip_longest(*[f] * 10):
                futures = [
                    loop.run_in_executor(None, requests.get, f"http://{url.strip()}") for url in next_n_lines
                ]
                try:

                    responses = await asyncio.gather(*[asyncio.wrap_future(future) for future in futures], return_exceptions=True)
                except Exception as e:
                    print(f'exception: {e}')
                processed_line_count += len(responses)

                for response in responses:
                    try:
                        if response.status_code < 400:
                            regex_result = __execute_regex(response.text)
                            title = __get_title(response)
                            state = False
                            if len(regex_result) != 0:
                                state = True
                            __save_content({
                                "domain_name": response.url,
                                "status_code": response.status_code,
                                "title": title,
                                "content": response.text,
                                "is_it_key": state,
                                "is_active": True,
                                "extra_info": regex_result
                            })
                    except:
                        print("1")
                responses = []
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

if __name__ == '__main__':
    app = create_app()
    tracemalloc.start()
    file_path = app.config['DOMAIN_NAMES_STATIC_FILE_PATH']
    app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'implicit_returning': False}
    with app.app_context():
        search_domain_content(file_path)
