#coding=utf8
# import random
# import os
# from bs4 import BeautifulSoup
# from itertools import cycle
from flask import Flask
from flask import render_template
from flask import request
from word2vec import word2vec_vote
import flask
app = Flask(__name__)

# ================================================================
vote = word2vec_vote()
vote.load_model("2016PE_news_cuted.model")

@app.route('/vote2016/')
def sim():
    return render_template('vote.html')

def reporter(result):
    return "<br>".join([ "{0:>5},{1:>5}".format(pair[0],round(pair[1],2)) for pair in result ])


@app.route('/vote2016/handler/',methods=['POST'])
def sim_handler():
    query = request.form['query'].encode("utf8")
    # print query
    # print [query]
    # print type(query)
    query = query.split()
    result = None
    if len(query) == 1:
        result = vote.sim(query[0])
    else:
        result = vote.infer(query[0],query[1],query[2])

    return reporter(result)

"""
def rs():
    if request.method == 'GET' and request.args.get('opt'):
        slot_candidate = request.args.get('opt')
        # print [slot_candidate]
        if len(slot_candidate) > 0:
            slot_candidate = slot_candidate.replace("|","\n")
            # print [slot_candidate]
            return handler_core(slot_candidate)

    return handler_core("Apple\nOrange\nBanana")

def handler_core(slot_candidate,title=TITLE):
    slot_candidate.strip()
    split_candidate = slot_candidate.split('\n')
    random.shuffle(split_candidate)
    split_candidate.append("")
    # print split_candidate
    render_coler = ["#FFCE29","#FFA22B","#FF8645","#FF6D3F","#FF494C","#FF3333","#FF0000"]
    cle = cycle(render_coler)
    slot_list = [ (idx+1,sc,cle.next()) for idx,sc in enumerate(split_candidate) ]
    # print slot_list

    # html = render_template('rs.html',slot_list=slot_list,slot_candidate=slot_candidate,title=title,debug_info=str(REDIS_URL))
    html = render_template('rs.html',slot_list=slot_list,slot_candidate=slot_candidate,title=title,base_url=request.base_url,debug_info=None)
    return html

@app.route('/rs/rs_handler/',methods=['POST'])
def rs_handler():
    slot_candidate = request.form['slot_candidate']
    title = request.form['title'] if request.form['title'] else TITLE
    html = handler_core(slot_candidate,title)
    soup = BeautifulSoup(html)
    body = str(soup.find("body"))
    # print html
    return body

@app.route('/rs/nccu_eat/')
def nccu_eat():
    slot_candidate = u"\n".join([u"45大街",u"華越",u"金鮨"])
    return handler_core(slot_candidate=slot_candidate,title="NCCU Restaurant Selector")

@app.route('/rs/age3/ch/')
def age3_ch():
    slot_candidate = u"\n".join([u"英國",u"法國",u"德國",u"俄國",u"荷蘭",u"西班牙",u"葡萄牙",u"鄂圖曼",u"阿茲特克",u"易落魁",u"蘇族",u"中國",u"日本",u"印度"])
    return handler_core(slot_candidate=slot_candidate,title="Age 3 civilization Selector")

@app.route('/rs/age3/en/')
def age3_en():
    slot_candidate = u"\n".join([u"British",u"French",u"Germans",u"Russians",u"Dutch",u"Spanish",u"Portuguese",u"Ottomans",u"Aztec",u"Iroquois",u"Sioux",u"Chinese",u"Japanese",u"Indians"])
    return handler_core(slot_candidate=slot_candidate,title="Age 3 civilization Selector")
"""
# ================================================================


if __name__ == "__main__":
    app.run(debug=True)

    # port = int(os.environ.get("PORT", 5000))
    # app.run(host='0.0.0.0', port=port)
