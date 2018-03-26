from enhancements import BaseEnhancement
import WSClient
import pprint


class clientAlias(BaseEnhancement):
    def process(self, match):
        if 'client_name' in match:
            ws = WSClient.Vtiger_WSClient('https://vtiger.iinfosec.net/')
            ws.doLogin('reports', 'kXtfcZseUTMwzUJW')
            vt_account = ws.doQuery("select * from Accounts where cf_1072='" +
                                    match['client_name'] + "';")
            # concat emails to string and place in match body
            emails = vt_account[0]['cf_1046'] + ', ' + vt_account[0]['cf_1048'] + ', ' + vt_account[0]['cf_1070']
            match['email'] = emails
            pprint.pprint(match)
