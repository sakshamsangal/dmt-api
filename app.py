import os

from flask import Flask, request, jsonify

from dao import create as cr
from dao import delete as dt
from dao import export as ex
from dao import update as ud
from service import fill_comp_style as fcs
from service import fill_feat as ff
from service import fill_phase as fp
from service import map_tag as mt1
from service import map_xpath as mx1
from service import my_convert as mc1
from service import xml_split as chunk
from service import xml_split_with_root as chunk_root
from service.master import create_master_att as cma
from service.master import create_master_pc as cmp
from service.master import create_master_tag as cmt

app = Flask(__name__)


@app.route('/export', methods=["POST"])
def export_tb_map_tag():
    try:
        if request.method == "POST":
            loc = request.json['loc']
            ct = request.json['ct']
            tb_name = request.json['tb_name']
            ex.export_tb_map_tag(loc, ct, tb_name)
            return jsonify({'status': f'{tb_name} exported as excel', 'loc': f'{loc}/excel'})
    except Exception as e:
        return jsonify({'status': str(e)})


@app.route('/dir-maker', methods=["POST"])
def dir_maker():
    try:
        if request.method == "POST":
            ls = request.json['folder_name']
            loc = request.json['loc']
            for x in ls:
                for item in ['xml', 'excel', 'word', 'pdf', 'res']:
                    os.makedirs(f'{loc}/{x}/{item}', exist_ok=True)
                os.makedirs(f'{loc}/{x}/xml/ox_{x}', exist_ok=True)
                os.makedirs(f'{loc}/{x}/xml/cx_{x}', exist_ok=True)
                os.makedirs(f'{loc}/{x}/xml/zx_{x}', exist_ok=True)
            return {'folder_name': ls, 'loc': loc, 'status': 'created'}
    except Exception as e:
        return jsonify({'status': str(e)})


@app.route('/xml-chunk', methods=["POST"])
def xml_chunk():
    try:
        if request.method == "POST":
            ct = request.json['ct']
            loc = request.json['loc']
            tag_selected = request.json['tag_selected']
            prod_names = request.json['prod_names']
            all_dir = request.json['all-dir']
            chunk.process_xml_chunk(loc, ct, tag_selected, all_dir, prod_names)
            return {'ct': ct, 'loc': loc, 'status': True, 'tag_selected': tag_selected}
    except Exception as e:
        return jsonify({'status': str(e)})


@app.route('/xml-chunk-root', methods=["POST"])
def xml_chunk_root():
    try:
        if request.method == "POST":
            ct = request.json['ct']
            loc = request.json['loc']
            ls_tag = request.json['ls_tag']
            prod_names = request.json['prod_names']
            all_dir = request.json['all-dir']
            chunk_root.process_xml_chunk_root(loc, ct, ls_tag, all_dir, prod_names)
            return {'ct': ct, 'loc': loc, 'status': True, 'tag_selected': ls_tag}
    except Exception as e:
        return jsonify({'status': str(e)})


@app.route("/data-dic-add-col", methods=["POST"])
def data_dic_add_col():
    try:
        if request.method == "POST":
            loc = request.json['loc']
            ct = request.json['ct']
            cr.create_all_tb(loc)
            x = cr.add_column(loc, ct, 'tb_data_dic')
            return jsonify({'status': x})
    except Exception as e:
        return jsonify({'status': str(e)})


@app.route("/convert-dd-to-tm", methods=["POST"])
def convert_dd_to_tm():
    try:
        if request.method == "POST":
            loc = request.json['loc']
            ct = request.json['ct']
            res = mc1.convert_dd_to_tm(loc, ct)
            return {'status': res}
    except Exception as e:
        return jsonify({'status': str(e)})


@app.route("/convert-tm-to-dd", methods=["POST"])
def convert_tm_to_dd():
    try:
        if request.method == "POST":
            loc = request.json['loc']
            ct = request.json['ct']
            res = mc1.convert_tm_to_dd(loc, ct)
            return {'status': res}

    except Exception as e:
        return jsonify({'status': str(e)})


@app.route("/map-xpath", methods=["POST"])
def map_xpath():
    try:
        if request.method == "POST":
            loc = request.json['loc']
            ct = request.json['ct']
            file_name = request.json['file_name']
            sn = request.json['sn']
            res = mx1.map_xpath_to_tag(loc, ct, file_name, sn)
            return {'status': res}
    except Exception as e:
        return jsonify({'status': str(e)})


@app.route("/map-tag", methods=["POST"])
def map_tag():
    try:
        if request.method == "POST":
            loc = request.json['loc']
            ct = request.json['ct']
            res = mt1.map_tag(loc, ct)
            return {'status': res}
    except Exception as e:
        return jsonify({'status': str(e)})


@app.route("/fill-feat", methods=["POST"])
def fill_feat():
    try:
        if request.method == "POST":
            loc = request.json['loc']
            ct = request.json['ct']
            ls = ff.fill_feature(loc, ct)
            return {'pat': ls}
    except Exception as e:
        return jsonify({'status': str(e)})


@app.route("/fill-comp-style", methods=["POST"])
def fill_comp_style():
    try:
        if request.method == "POST":
            loc = request.json['loc']
            ct = request.json['ct']
            fn = request.json['fn']
            ls, fc = fcs.fill_comp_style(loc, ct, fn)
            return {'xpath_left': ls, 'false_count':fc}
    except Exception as e:
        return jsonify({'status': str(e)})


@app.route("/fill-phase", methods=["POST"])
def fill_phase():
    try:
        if request.method == "POST":
            loc = request.json['loc']
            ct = request.json['ct']
            alpha_no = request.json['alpha_no']
            ls = fp.fill_phase(loc, ct, alpha_no)
            return {'xpath_left': ls}
    except Exception as e:
        return jsonify({'status': str(e)})


@app.route("/master-tag", methods=["POST"])
def master_tag():
    try:
        if request.method == "POST":
            loc = request.json['loc']
            ct = request.json['ct']
            prod = request.json['prod']
            all_dir = request.json['all-dir']
            cmt.process_master_tag(loc, ct, all_dir, prod)
            return jsonify({'status': 'db updated'})
    except Exception as e:
        return jsonify({'status': str(e)})


@app.route("/master-att", methods=["POST"])
def master_att():
    try:
        if request.method == "POST":
            ct = request.json['ct']
            loc = request.json['loc']
            prod = request.json['prod']
            all_dir = request.json['all-dir']
            cma.process_master_att(loc, ct, all_dir, prod)
            return jsonify({'status': 'db updated'})
    except Exception as e:
        return jsonify({'status': str(e)})


@app.route("/master-pc", methods=["POST"])
def master_pc():
    try:
        if request.method == "POST":
            ct = request.json['ct']
            loc = request.json['loc']
            prod = request.json['prod']
            all_dir = request.json['all-dir']
            cmp.process_master_pc(loc, ct, all_dir, prod)
            return jsonify({'status': 'db updated'})
    except Exception as e:
        return jsonify({'status': str(e)})


@app.route("/delete-prod", methods=["POST"])
def delete_prod():
    try:
        if request.method == "POST":
            loc = request.json['loc']
            ls = request.json['prod_name']
            temp = []
            for x in ls:
                temp.append((x,))
            msg = dt.delete_prod(loc, temp)
            return {'status': msg}
    except Exception as e:
        return jsonify({'status': str(e)})


@app.route("/delete-ct", methods=["POST"])
def delete_ct():
    try:
        if request.method == "POST":
            loc = request.json['loc']
            ls = request.json['ct']
            mt = request.json['mt']
            temp = []
            for x in ls:
                temp.append((x,))
            dt.delete_ct(loc, temp, mt)
            ud.update_processed_remove(loc, ls, mt, 0)
            return {'status': True}
    except Exception as e:
        return jsonify({'status': str(e)})


if __name__ == '__main__':
    app.run()
