from urllib2 import urlopen, Request
                        headers = {'Authorization': 'Token token=c20501a6d78fea8248ebe0910b1d4de1'}
                        # Pesquisa de CEP pelo número
                        url = "http://www.cepaberto.com/api/v2/ceps.json?cep=40010000"
                        json = urlopen(Request(url, None, headers=headers)).read()
                        print json
                    