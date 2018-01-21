from elastalert.enhancements import BaseEnhancement
import WSClient


class MyEnhancement(BaseEnhancement):
    # The enhancement is run against every match
    # ElastAlert will do this for each enhancement linked to a rule

    def process(self, match):
        if 'client_name' in match:
            ws = WSClient.Vtiger_WSClient('https://vtiger.iinfosec.net/')
            ws.doLogin('reports', 'kXtfcZseUTMwzUJW')
            vt_account = ws.doQuery("select * from Accounts where cf_1072='" +
                                    match['client_name'] + "';")
            match['email'][0] = vt_account[0]['cf_1046']
            match['email'][1] = vt_account[0]['cf_1048']
            match['email'][2] = vt_account[0]['cf_1070']
