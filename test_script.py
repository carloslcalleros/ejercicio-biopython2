import unittest
import os
from script import summarize_contents

class Prueba(unittest.TestCase):
	def test_summarize_contents(self):
		d1 = {'File:': 'AF323668.gbk', 'Path:': os.path.abspath('data'), 'Num_records:': 1, 'Names:': ['AF323668'], 'IDs:': ['AF323668.1'], 'Descriptions': ['Bacteriophage bIL285, complete genome']}
		s = summarize_contents(os.path.abspath("data/AF323668.gbk"))
		self.assertDictEqual(d1, s)

		d2 = {'File:': 'NC_002703.gbk', 'Path:': os.path.abspath('data'), 'Num_records:': 1, 'Names:': ['NC_002703'], 'IDs:': ['NC_002703.1'], 'Descriptions': ['Lactococcus phage Tuc2009, complete genome']}
		s = summarize_contents(os.path.abspath("data/NC_002703.gbk"))
		self.assertDictEqual(d2, s)

		d3 = {'File:': 'ls_orchid.gbk', 'Path:': os.path.abspath('data'), 'Num_records:': 94, 'Names:': ['Z78533', 'Z78532', 'Z78531', 'Z78530', 'Z78529', 'Z78527', 'Z78526', 'Z78525', 'Z78524', 'Z78523', 'Z78522', 'Z78521', 'Z78520', 'Z78519', 'Z78518', 'Z78517', 'Z78516', 'Z78515', 'Z78514', 'Z78513', 'Z78512', 'Z78511', 'Z78510', 'Z78509', 'Z78508', 'Z78507', 'Z78506', 'Z78505', 'Z78504', 'Z78503', 'Z78502', 'Z78501', 'Z78500', 'Z78499', 'Z78498', 'Z78497', 'Z78496', 'Z78495', 'Z78494', 'Z78493', 'Z78492', 'Z78491', 'Z78490', 'Z78489', 'Z78488', 'Z78487', 'Z78486', 'Z78485', 'Z78484', 'Z78483', 'Z78482', 'Z78481', 'Z78480', 'Z78479', 'Z78478', 'Z78477', 'Z78476', 'Z78475', 'Z78474', 'Z78473', 'Z78472', 'Z78471', 'Z78470', 'Z78469', 'Z78468', 'Z78467', 'Z78466', 'Z78465', 'Z78464', 'Z78463', 'Z78462', 'Z78461', 'Z78460', 'Z78459', 'Z78458', 'Z78457', 'Z78456', 'Z78455', 'Z78454', 'Z78453', 'Z78452', 'Z78451', 'Z78450', 'Z78449', 'Z78448', 'Z78447', 'Z78446', 'Z78445', 'Z78444', 'Z78443', 'Z78442', 'Z78441', 'Z78440', 'Z78439'], 'IDs:': ['Z78533.1', 'Z78532.1', 'Z78531.1', 'Z78530.1', 'Z78529.1', 'Z78527.1', 'Z78526.1', 'Z78525.1', 'Z78524.1', 'Z78523.1', 'Z78522.1', 'Z78521.1', 'Z78520.1', 'Z78519.1', 'Z78518.1', 'Z78517.1', 'Z78516.1', 'Z78515.1', 'Z78514.1', 'Z78513.1', 'Z78512.1', 'Z78511.1', 'Z78510.1', 'Z78509.1', 'Z78508.1', 'Z78507.1', 'Z78506.1', 'Z78505.1', 'Z78504.1', 'Z78503.1', 'Z78502.1', 'Z78501.1', 'Z78500.1', 'Z78499.1', 'Z78498.1', 'Z78497.1', 'Z78496.1', 'Z78495.1', 'Z78494.1', 'Z78493.1', 'Z78492.1', 'Z78491.1', 'Z78490.1', 'Z78489.1', 'Z78488.1', 'Z78487.1', 'Z78486.1', 'Z78485.1', 'Z78484.1', 'Z78483.1', 'Z78482.1', 'Z78481.1', 'Z78480.1', 'Z78479.1', 'Z78478.1', 'Z78477.1', 'Z78476.1', 'Z78475.1', 'Z78474.1', 'Z78473.1', 'Z78472.1', 'Z78471.1', 'Z78470.1', 'Z78469.1', 'Z78468.1', 'Z78467.1', 'Z78466.1', 'Z78465.1', 'Z78464.1', 'Z78463.1', 'Z78462.1', 'Z78461.1', 'Z78460.1', 'Z78459.1', 'Z78458.1', 'Z78457.1', 'Z78456.1', 'Z78455.1', 'Z78454.1', 'Z78453.1', 'Z78452.1', 'Z78451.1', 'Z78450.1', 'Z78449.1', 'Z78448.1', 'Z78447.1', 'Z78446.1', 'Z78445.1', 'Z78444.1', 'Z78443.1', 'Z78442.1', 'Z78441.1', 'Z78440.1', 'Z78439.1'], 'Descriptions': ['C.irapeanum 5.8S rRNA gene and ITS1 and ITS2 DNA', 'C.californicum 5.8S rRNA gene and ITS1 and ITS2 DNA', 'C.fasciculatum 5.8S rRNA gene and ITS1 and ITS2 DNA', 'C.margaritaceum 5.8S rRNA gene and ITS1 and ITS2 DNA', 'C.lichiangense 5.8S rRNA gene and ITS1 and ITS2 DNA', 'C.yatabeanum 5.8S rRNA gene and ITS1 and ITS2 DNA', 'C.guttatum 5.8S rRNA gene and ITS1 and ITS2 DNA', 'C.acaule 5.8S rRNA gene and ITS1 and ITS2 DNA', 'C.formosanum 5.8S rRNA gene and ITS1 and ITS2 DNA', 'C.himalaicum 5.8S rRNA gene and ITS1 and ITS2 DNA', 'C.macranthum 5.8S rRNA gene and ITS1 and ITS2 DNA', 'C.calceolus 5.8S rRNA gene and ITS1 and ITS2 DNA', 'C.segawai 5.8S rRNA gene and ITS1 and ITS2 DNA', 'C.pubescens 5.8S rRNA gene and ITS1 and ITS2 DNA', 'C.reginae 5.8S rRNA gene and ITS1 and ITS2 DNA', 'C.flavum 5.8S rRNA gene and ITS1 and ITS2 DNA', 'C.passerinum 5.8S rRNA gene and ITS1 and ITS2 DNA', 'M.xerophyticum 5.8S rRNA gene and ITS1 and ITS2 DNA', 'P.schlimii 5.8S rRNA gene and ITS1 and ITS2 DNA', 'P.besseae 5.8S rRNA gene and ITS1 and ITS2 DNA', 'P.wallisii 5.8S rRNA gene and ITS1 and ITS2 DNA', 'P.exstaminodium 5.8S rRNA gene and ITS1 and ITS2 DNA', 'P.caricinum 5.8S rRNA gene and ITS1 and ITS2 DNA', 'P.pearcei 5.8S rRNA gene and ITS1 and ITS2 DNA', 'P.longifolium 5.8S rRNA gene and ITS1 and ITS2 DNA', 'P.lindenii 5.8S rRNA gene and ITS1 and ITS2 DNA', 'P.lindleyanum 5.8S rRNA gene and ITS1 and ITS2 DNA', 'P.sargentianum 5.8S rRNA gene and ITS1 and ITS2 DNA', 'P.kaiteurum 5.8S rRNA gene and ITS1 and ITS2 DNA', 'P.czerwiakowianum 5.8S rRNA gene and ITS1 and ITS2 DNA', 'P.boissierianum 5.8S rRNA gene and ITS1 and ITS2 DNA', 'P.caudatum 5.8S rRNA gene and ITS1 and ITS2 DNA', 'P.warszewiczianum 5.8S rRNA gene and ITS1 and ITS2 DNA', 'P.micranthum 5.8S rRNA gene and ITS1 and ITS2 DNA', 'P.malipoense 5.8S rRNA gene and ITS1 and ITS2 DNA', 'P.delenatii 5.8S rRNA gene and ITS1 and ITS2 DNA', 'P.armeniacum 5.8S rRNA gene and ITS1 and ITS2 DNA', 'P.emersonii 5.8S rRNA gene and ITS1 and ITS2 DNA', 'P.niveum 5.8S rRNA gene and ITS1 and ITS2 DNA', 'P.godefroyae 5.8S rRNA gene and ITS1 and ITS2 DNA', 'P.bellatulum 5.8S rRNA gene and ITS1 and ITS2 DNA', 'P.concolor 5.8S rRNA gene and ITS1 and ITS2 DNA', 'P.fairrieanum 5.8S rRNA gene and ITS1 and ITS2 DNA', 'P.druryi 5.8S rRNA gene and ITS1 and ITS2 DNA', 'P.tigrinum 5.8S rRNA gene and ITS1 and ITS2 DNA', 'P.hirsutissimum 5.8S rRNA gene and ITS1 and ITS2 DNA', 'P.barbigerum 5.8S rRNA gene and ITS1 and ITS2 DNA', 'P.henryanum 5.8S rRNA gene and ITS1 and ITS2 DNA', 'P.charlesworthii 5.8S rRNA gene and ITS1 and ITS2 DNA', 'P.villosum 5.8S rRNA gene and ITS1 and ITS2 DNA', 'P.exul 5.8S rRNA gene and ITS1 and ITS2 DNA', 'P.insigne 5.8S rRNA gene and ITS1 and ITS2 DNA', 'P.gratrixianum 5.8S rRNA gene and ITS1 and ITS2 DNA', 'P.primulinum 5.8S rRNA gene and ITS1 and ITS2 DNA', 'P.victoria 5.8S rRNA gene and ITS1 and ITS2 DNA', 'P.victoria 5.8S rRNA gene and ITS1 and ITS2 DNA', 'P.glaucophyllum 5.8S rRNA gene and ITS1 and ITS2 DNA', 'P.supardii 5.8S rRNA gene and ITS1 and ITS2 DNA', 'P.kolopakingii 5.8S rRNA gene and ITS1 and ITS2 DNA', 'P.sanderianum 5.8S rRNA gene and ITS1 and ITS2 DNA', 'P.lowii 5.8S rRNA gene and ITS1 and ITS2 DNA', 'P.dianthum 5.8S rRNA gene and ITS1 and ITS2 DNA', 'P.parishii 5.8S rRNA gene and ITS1 and ITS2 DNA', 'P.haynaldianum 5.8S rRNA gene and ITS1 and ITS2 DNA', 'P.adductum 5.8S rRNA gene and ITS1 and ITS2 DNA', 'P.stonei 5.8S rRNA gene and ITS1 and ITS2 DNA', 'P.philippinense 5.8S rRNA gene and ITS1 and ITS2 DNA', 'P.rothschildianum 5.8S rRNA gene and ITS1 and ITS2 DNA', 'P.glanduliferum 5.8S rRNA gene and ITS1 and ITS2 DNA', 'P.glanduliferum 5.8S rRNA gene and ITS1 and ITS2 DNA', 'P.sukhakulii 5.8S rRNA gene and ITS1 and ITS2 DNA', 'P.wardii 5.8S rRNA gene and ITS1 and ITS2 DNA', 'P.ciliolare 5.8S rRNA gene and ITS1 and ITS2 DNA', 'P.dayanum 5.8S rRNA gene and ITS1 and ITS2 DNA', 'P.hennisianum 5.8S rRNA gene and ITS1 and ITS2 DNA', 'P.callosum 5.8S rRNA gene and ITS1 and ITS2 DNA', 'P.tonsum 5.8S rRNA gene and ITS1 and ITS2 DNA', 'P.javanicum 5.8S rRNA gene and ITS1 and ITS2 DNA', 'P.fowliei 5.8S rRNA gene and ITS1 and ITS2 DNA', 'P.schoseri 5.8S rRNA gene and ITS1 and ITS2 DNA', 'P.bougainvilleanum 5.8S rRNA gene and ITS1 and ITS2 DNA', 'P.hookerae 5.8S rRNA gene and ITS1 and ITS2 DNA', 'P.papuanum 5.8S rRNA gene and ITS1 and ITS2 DNA', 'P.mastersianum 5.8S rRNA gene and ITS1 and ITS2 DNA', 'P.argus 5.8S rRNA gene and ITS1 and ITS2 DNA', 'P.venustum 5.8S rRNA gene and ITS1 and ITS2 DNA', 'P.acmodontum 5.8S rRNA gene and ITS1 and ITS2 DNA', 'P.urbanianum 5.8S rRNA gene and ITS1 and ITS2 DNA', 'P.appletonianum 5.8S rRNA gene and ITS1 and ITS2 DNA', 'P.lawrenceanum 5.8S rRNA gene and ITS1 and ITS2 DNA', 'P.bullenianum 5.8S rRNA gene and ITS1 and ITS2 DNA', 'P.superbiens 5.8S rRNA gene and ITS1 and ITS2 DNA', 'P.purpuratum 5.8S rRNA gene and ITS1 and ITS2 DNA', 'P.barbatum 5.8S rRNA gene and ITS1 and ITS2 DNA']}
		s = summarize_contents(os.path.abspath("data/ls_orchid.gbk"))
		self.assertDictEqual(d3, s)

		d4 = {'File:': 'ls_orchid.fasta', 'Path:': os.path.abspath('data'), 'Num_records:': 94, 'Names:': ['gi|2765658|emb|Z78533.1|CIZ78533', 'gi|2765657|emb|Z78532.1|CCZ78532', 'gi|2765656|emb|Z78531.1|CFZ78531', 'gi|2765655|emb|Z78530.1|CMZ78530', 'gi|2765654|emb|Z78529.1|CLZ78529', 'gi|2765652|emb|Z78527.1|CYZ78527', 'gi|2765651|emb|Z78526.1|CGZ78526', 'gi|2765650|emb|Z78525.1|CAZ78525', 'gi|2765649|emb|Z78524.1|CFZ78524', 'gi|2765648|emb|Z78523.1|CHZ78523', 'gi|2765647|emb|Z78522.1|CMZ78522', 'gi|2765646|emb|Z78521.1|CCZ78521', 'gi|2765645|emb|Z78520.1|CSZ78520', 'gi|2765644|emb|Z78519.1|CPZ78519', 'gi|2765643|emb|Z78518.1|CRZ78518', 'gi|2765642|emb|Z78517.1|CFZ78517', 'gi|2765641|emb|Z78516.1|CPZ78516', 'gi|2765640|emb|Z78515.1|MXZ78515', 'gi|2765639|emb|Z78514.1|PSZ78514', 'gi|2765638|emb|Z78513.1|PBZ78513', 'gi|2765637|emb|Z78512.1|PWZ78512', 'gi|2765636|emb|Z78511.1|PEZ78511', 'gi|2765635|emb|Z78510.1|PCZ78510', 'gi|2765634|emb|Z78509.1|PPZ78509', 'gi|2765633|emb|Z78508.1|PLZ78508', 'gi|2765632|emb|Z78507.1|PLZ78507', 'gi|2765631|emb|Z78506.1|PLZ78506', 'gi|2765630|emb|Z78505.1|PSZ78505', 'gi|2765629|emb|Z78504.1|PKZ78504', 'gi|2765628|emb|Z78503.1|PCZ78503', 'gi|2765627|emb|Z78502.1|PBZ78502', 'gi|2765626|emb|Z78501.1|PCZ78501', 'gi|2765625|emb|Z78500.1|PWZ78500', 'gi|2765624|emb|Z78499.1|PMZ78499', 'gi|2765623|emb|Z78498.1|PMZ78498', 'gi|2765622|emb|Z78497.1|PDZ78497', 'gi|2765621|emb|Z78496.1|PAZ78496', 'gi|2765620|emb|Z78495.1|PEZ78495', 'gi|2765619|emb|Z78494.1|PNZ78494', 'gi|2765618|emb|Z78493.1|PGZ78493', 'gi|2765617|emb|Z78492.1|PBZ78492', 'gi|2765616|emb|Z78491.1|PCZ78491', 'gi|2765615|emb|Z78490.1|PFZ78490', 'gi|2765614|emb|Z78489.1|PDZ78489', 'gi|2765613|emb|Z78488.1|PTZ78488', 'gi|2765612|emb|Z78487.1|PHZ78487', 'gi|2765611|emb|Z78486.1|PBZ78486', 'gi|2765610|emb|Z78485.1|PHZ78485', 'gi|2765609|emb|Z78484.1|PCZ78484', 'gi|2765608|emb|Z78483.1|PVZ78483', 'gi|2765607|emb|Z78482.1|PEZ78482', 'gi|2765606|emb|Z78481.1|PIZ78481', 'gi|2765605|emb|Z78480.1|PGZ78480', 'gi|2765604|emb|Z78479.1|PPZ78479', 'gi|2765603|emb|Z78478.1|PVZ78478', 'gi|2765602|emb|Z78477.1|PVZ78477', 'gi|2765601|emb|Z78476.1|PGZ78476', 'gi|2765600|emb|Z78475.1|PSZ78475', 'gi|2765599|emb|Z78474.1|PKZ78474', 'gi|2765598|emb|Z78473.1|PSZ78473', 'gi|2765597|emb|Z78472.1|PLZ78472', 'gi|2765596|emb|Z78471.1|PDZ78471', 'gi|2765595|emb|Z78470.1|PPZ78470', 'gi|2765594|emb|Z78469.1|PHZ78469', 'gi|2765593|emb|Z78468.1|PAZ78468', 'gi|2765592|emb|Z78467.1|PSZ78467', 'gi|2765591|emb|Z78466.1|PPZ78466', 'gi|2765590|emb|Z78465.1|PRZ78465', 'gi|2765589|emb|Z78464.1|PGZ78464', 'gi|2765588|emb|Z78463.1|PGZ78463', 'gi|2765587|emb|Z78462.1|PSZ78462', 'gi|2765586|emb|Z78461.1|PWZ78461', 'gi|2765585|emb|Z78460.1|PCZ78460', 'gi|2765584|emb|Z78459.1|PDZ78459', 'gi|2765583|emb|Z78458.1|PHZ78458', 'gi|2765582|emb|Z78457.1|PCZ78457', 'gi|2765581|emb|Z78456.1|PTZ78456', 'gi|2765580|emb|Z78455.1|PJZ78455', 'gi|2765579|emb|Z78454.1|PFZ78454', 'gi|2765578|emb|Z78453.1|PSZ78453', 'gi|2765577|emb|Z78452.1|PBZ78452', 'gi|2765576|emb|Z78451.1|PHZ78451', 'gi|2765575|emb|Z78450.1|PPZ78450', 'gi|2765574|emb|Z78449.1|PMZ78449', 'gi|2765573|emb|Z78448.1|PAZ78448', 'gi|2765572|emb|Z78447.1|PVZ78447', 'gi|2765571|emb|Z78446.1|PAZ78446', 'gi|2765570|emb|Z78445.1|PUZ78445', 'gi|2765569|emb|Z78444.1|PAZ78444', 'gi|2765568|emb|Z78443.1|PLZ78443', 'gi|2765567|emb|Z78442.1|PBZ78442', 'gi|2765566|emb|Z78441.1|PSZ78441', 'gi|2765565|emb|Z78440.1|PPZ78440', 'gi|2765564|emb|Z78439.1|PBZ78439'], 'IDs:': ['gi|2765658|emb|Z78533.1|CIZ78533', 'gi|2765657|emb|Z78532.1|CCZ78532', 'gi|2765656|emb|Z78531.1|CFZ78531', 'gi|2765655|emb|Z78530.1|CMZ78530', 'gi|2765654|emb|Z78529.1|CLZ78529', 'gi|2765652|emb|Z78527.1|CYZ78527', 'gi|2765651|emb|Z78526.1|CGZ78526', 'gi|2765650|emb|Z78525.1|CAZ78525', 'gi|2765649|emb|Z78524.1|CFZ78524', 'gi|2765648|emb|Z78523.1|CHZ78523', 'gi|2765647|emb|Z78522.1|CMZ78522', 'gi|2765646|emb|Z78521.1|CCZ78521', 'gi|2765645|emb|Z78520.1|CSZ78520', 'gi|2765644|emb|Z78519.1|CPZ78519', 'gi|2765643|emb|Z78518.1|CRZ78518', 'gi|2765642|emb|Z78517.1|CFZ78517', 'gi|2765641|emb|Z78516.1|CPZ78516', 'gi|2765640|emb|Z78515.1|MXZ78515', 'gi|2765639|emb|Z78514.1|PSZ78514', 'gi|2765638|emb|Z78513.1|PBZ78513', 'gi|2765637|emb|Z78512.1|PWZ78512', 'gi|2765636|emb|Z78511.1|PEZ78511', 'gi|2765635|emb|Z78510.1|PCZ78510', 'gi|2765634|emb|Z78509.1|PPZ78509', 'gi|2765633|emb|Z78508.1|PLZ78508', 'gi|2765632|emb|Z78507.1|PLZ78507', 'gi|2765631|emb|Z78506.1|PLZ78506', 'gi|2765630|emb|Z78505.1|PSZ78505', 'gi|2765629|emb|Z78504.1|PKZ78504', 'gi|2765628|emb|Z78503.1|PCZ78503', 'gi|2765627|emb|Z78502.1|PBZ78502', 'gi|2765626|emb|Z78501.1|PCZ78501', 'gi|2765625|emb|Z78500.1|PWZ78500', 'gi|2765624|emb|Z78499.1|PMZ78499', 'gi|2765623|emb|Z78498.1|PMZ78498', 'gi|2765622|emb|Z78497.1|PDZ78497', 'gi|2765621|emb|Z78496.1|PAZ78496', 'gi|2765620|emb|Z78495.1|PEZ78495', 'gi|2765619|emb|Z78494.1|PNZ78494', 'gi|2765618|emb|Z78493.1|PGZ78493', 'gi|2765617|emb|Z78492.1|PBZ78492', 'gi|2765616|emb|Z78491.1|PCZ78491', 'gi|2765615|emb|Z78490.1|PFZ78490', 'gi|2765614|emb|Z78489.1|PDZ78489', 'gi|2765613|emb|Z78488.1|PTZ78488', 'gi|2765612|emb|Z78487.1|PHZ78487', 'gi|2765611|emb|Z78486.1|PBZ78486', 'gi|2765610|emb|Z78485.1|PHZ78485', 'gi|2765609|emb|Z78484.1|PCZ78484', 'gi|2765608|emb|Z78483.1|PVZ78483', 'gi|2765607|emb|Z78482.1|PEZ78482', 'gi|2765606|emb|Z78481.1|PIZ78481', 'gi|2765605|emb|Z78480.1|PGZ78480', 'gi|2765604|emb|Z78479.1|PPZ78479', 'gi|2765603|emb|Z78478.1|PVZ78478', 'gi|2765602|emb|Z78477.1|PVZ78477', 'gi|2765601|emb|Z78476.1|PGZ78476', 'gi|2765600|emb|Z78475.1|PSZ78475', 'gi|2765599|emb|Z78474.1|PKZ78474', 'gi|2765598|emb|Z78473.1|PSZ78473', 'gi|2765597|emb|Z78472.1|PLZ78472', 'gi|2765596|emb|Z78471.1|PDZ78471', 'gi|2765595|emb|Z78470.1|PPZ78470', 'gi|2765594|emb|Z78469.1|PHZ78469', 'gi|2765593|emb|Z78468.1|PAZ78468', 'gi|2765592|emb|Z78467.1|PSZ78467', 'gi|2765591|emb|Z78466.1|PPZ78466', 'gi|2765590|emb|Z78465.1|PRZ78465', 'gi|2765589|emb|Z78464.1|PGZ78464', 'gi|2765588|emb|Z78463.1|PGZ78463', 'gi|2765587|emb|Z78462.1|PSZ78462', 'gi|2765586|emb|Z78461.1|PWZ78461', 'gi|2765585|emb|Z78460.1|PCZ78460', 'gi|2765584|emb|Z78459.1|PDZ78459', 'gi|2765583|emb|Z78458.1|PHZ78458', 'gi|2765582|emb|Z78457.1|PCZ78457', 'gi|2765581|emb|Z78456.1|PTZ78456', 'gi|2765580|emb|Z78455.1|PJZ78455', 'gi|2765579|emb|Z78454.1|PFZ78454', 'gi|2765578|emb|Z78453.1|PSZ78453', 'gi|2765577|emb|Z78452.1|PBZ78452', 'gi|2765576|emb|Z78451.1|PHZ78451', 'gi|2765575|emb|Z78450.1|PPZ78450', 'gi|2765574|emb|Z78449.1|PMZ78449', 'gi|2765573|emb|Z78448.1|PAZ78448', 'gi|2765572|emb|Z78447.1|PVZ78447', 'gi|2765571|emb|Z78446.1|PAZ78446', 'gi|2765570|emb|Z78445.1|PUZ78445', 'gi|2765569|emb|Z78444.1|PAZ78444', 'gi|2765568|emb|Z78443.1|PLZ78443', 'gi|2765567|emb|Z78442.1|PBZ78442', 'gi|2765566|emb|Z78441.1|PSZ78441', 'gi|2765565|emb|Z78440.1|PPZ78440', 'gi|2765564|emb|Z78439.1|PBZ78439'], 'Descriptions': ['gi|2765658|emb|Z78533.1|CIZ78533 C.irapeanum 5.8S rRNA gene and ITS1 and ITS2 DNA', 'gi|2765657|emb|Z78532.1|CCZ78532 C.californicum 5.8S rRNA gene and ITS1 and ITS2 DNA', 'gi|2765656|emb|Z78531.1|CFZ78531 C.fasciculatum 5.8S rRNA gene and ITS1 and ITS2 DNA', 'gi|2765655|emb|Z78530.1|CMZ78530 C.margaritaceum 5.8S rRNA gene and ITS1 and ITS2 DNA', 'gi|2765654|emb|Z78529.1|CLZ78529 C.lichiangense 5.8S rRNA gene and ITS1 and ITS2 DNA', 'gi|2765652|emb|Z78527.1|CYZ78527 C.yatabeanum 5.8S rRNA gene and ITS1 and ITS2 DNA', 'gi|2765651|emb|Z78526.1|CGZ78526 C.guttatum 5.8S rRNA gene and ITS1 and ITS2 DNA', 'gi|2765650|emb|Z78525.1|CAZ78525 C.acaule 5.8S rRNA gene and ITS1 and ITS2 DNA', 'gi|2765649|emb|Z78524.1|CFZ78524 C.formosanum 5.8S rRNA gene and ITS1 and ITS2 DNA', 'gi|2765648|emb|Z78523.1|CHZ78523 C.himalaicum 5.8S rRNA gene and ITS1 and ITS2 DNA', 'gi|2765647|emb|Z78522.1|CMZ78522 C.macranthum 5.8S rRNA gene and ITS1 and ITS2 DNA', 'gi|2765646|emb|Z78521.1|CCZ78521 C.calceolus 5.8S rRNA gene and ITS1 and ITS2 DNA', 'gi|2765645|emb|Z78520.1|CSZ78520 C.segawai 5.8S rRNA gene and ITS1 and ITS2 DNA', 'gi|2765644|emb|Z78519.1|CPZ78519 C.pubescens 5.8S rRNA gene and ITS1 and ITS2 DNA', 'gi|2765643|emb|Z78518.1|CRZ78518 C.reginae 5.8S rRNA gene and ITS1 and ITS2 DNA', 'gi|2765642|emb|Z78517.1|CFZ78517 C.flavum 5.8S rRNA gene and ITS1 and ITS2 DNA', 'gi|2765641|emb|Z78516.1|CPZ78516 C.passerinum 5.8S rRNA gene and ITS1 and ITS2 DNA', 'gi|2765640|emb|Z78515.1|MXZ78515 M.xerophyticum 5.8S rRNA gene and ITS1 and ITS2 DNA', 'gi|2765639|emb|Z78514.1|PSZ78514 P.schlimii 5.8S rRNA gene and ITS1 and ITS2 DNA', 'gi|2765638|emb|Z78513.1|PBZ78513 P.besseae 5.8S rRNA gene and ITS1 and ITS2 DNA', 'gi|2765637|emb|Z78512.1|PWZ78512 P.wallisii 5.8S rRNA gene and ITS1 and ITS2 DNA', 'gi|2765636|emb|Z78511.1|PEZ78511 P.exstaminodium 5.8S rRNA gene and ITS1 and ITS2 DNA', 'gi|2765635|emb|Z78510.1|PCZ78510 P.caricinum 5.8S rRNA gene and ITS1 and ITS2 DNA', 'gi|2765634|emb|Z78509.1|PPZ78509 P.pearcei 5.8S rRNA gene and ITS1 and ITS2 DNA', 'gi|2765633|emb|Z78508.1|PLZ78508 P.longifolium 5.8S rRNA gene and ITS1 and ITS2 DNA', 'gi|2765632|emb|Z78507.1|PLZ78507 P.lindenii 5.8S rRNA gene and ITS1 and ITS2 DNA', 'gi|2765631|emb|Z78506.1|PLZ78506 P.lindleyanum 5.8S rRNA gene and ITS1 and ITS2 DNA', 'gi|2765630|emb|Z78505.1|PSZ78505 P.sargentianum 5.8S rRNA gene and ITS1 and ITS2 DNA', 'gi|2765629|emb|Z78504.1|PKZ78504 P.kaiteurum 5.8S rRNA gene and ITS1 and ITS2 DNA', 'gi|2765628|emb|Z78503.1|PCZ78503 P.czerwiakowianum 5.8S rRNA gene and ITS1 and ITS2 DNA', 'gi|2765627|emb|Z78502.1|PBZ78502 P.boissierianum 5.8S rRNA gene and ITS1 and ITS2 DNA', 'gi|2765626|emb|Z78501.1|PCZ78501 P.caudatum 5.8S rRNA gene and ITS1 and ITS2 DNA', 'gi|2765625|emb|Z78500.1|PWZ78500 P.warszewiczianum 5.8S rRNA gene and ITS1 and ITS2 DNA', 'gi|2765624|emb|Z78499.1|PMZ78499 P.micranthum 5.8S rRNA gene and ITS1 and ITS2 DNA', 'gi|2765623|emb|Z78498.1|PMZ78498 P.malipoense 5.8S rRNA gene and ITS1 and ITS2 DNA', 'gi|2765622|emb|Z78497.1|PDZ78497 P.delenatii 5.8S rRNA gene and ITS1 and ITS2 DNA', 'gi|2765621|emb|Z78496.1|PAZ78496 P.armeniacum 5.8S rRNA gene and ITS1 and ITS2 DNA', 'gi|2765620|emb|Z78495.1|PEZ78495 P.emersonii 5.8S rRNA gene and ITS1 and ITS2 DNA', 'gi|2765619|emb|Z78494.1|PNZ78494 P.niveum 5.8S rRNA gene and ITS1 and ITS2 DNA', 'gi|2765618|emb|Z78493.1|PGZ78493 P.godefroyae 5.8S rRNA gene and ITS1 and ITS2 DNA', 'gi|2765617|emb|Z78492.1|PBZ78492 P.bellatulum 5.8S rRNA gene and ITS1 and ITS2 DNA', 'gi|2765616|emb|Z78491.1|PCZ78491 P.concolor 5.8S rRNA gene and ITS1 and ITS2 DNA', 'gi|2765615|emb|Z78490.1|PFZ78490 P.fairrieanum 5.8S rRNA gene and ITS1 and ITS2 DNA', 'gi|2765614|emb|Z78489.1|PDZ78489 P.druryi 5.8S rRNA gene and ITS1 and ITS2 DNA', 'gi|2765613|emb|Z78488.1|PTZ78488 P.tigrinum 5.8S rRNA gene and ITS1 and ITS2 DNA', 'gi|2765612|emb|Z78487.1|PHZ78487 P.hirsutissimum 5.8S rRNA gene and ITS1 and ITS2 DNA', 'gi|2765611|emb|Z78486.1|PBZ78486 P.barbigerum 5.8S rRNA gene and ITS1 and ITS2 DNA', 'gi|2765610|emb|Z78485.1|PHZ78485 P.henryanum 5.8S rRNA gene and ITS1 and ITS2 DNA', 'gi|2765609|emb|Z78484.1|PCZ78484 P.charlesworthii 5.8S rRNA gene and ITS1 and ITS2 DNA', 'gi|2765608|emb|Z78483.1|PVZ78483 P.villosum 5.8S rRNA gene and ITS1 and ITS2 DNA', 'gi|2765607|emb|Z78482.1|PEZ78482 P.exul 5.8S rRNA gene and ITS1 and ITS2 DNA', 'gi|2765606|emb|Z78481.1|PIZ78481 P.insigne 5.8S rRNA gene and ITS1 and ITS2 DNA', 'gi|2765605|emb|Z78480.1|PGZ78480 P.gratrixianum 5.8S rRNA gene and ITS1 and ITS2 DNA', 'gi|2765604|emb|Z78479.1|PPZ78479 P.primulinum 5.8S rRNA gene and ITS1 and ITS2 DNA', 'gi|2765603|emb|Z78478.1|PVZ78478 P.victoria 5.8S rRNA gene and ITS1 and ITS2 DNA', 'gi|2765602|emb|Z78477.1|PVZ78477 P.victoria 5.8S rRNA gene and ITS1 and ITS2 DNA', 'gi|2765601|emb|Z78476.1|PGZ78476 P.glaucophyllum 5.8S rRNA gene and ITS1 and ITS2 DNA', 'gi|2765600|emb|Z78475.1|PSZ78475 P.supardii 5.8S rRNA gene and ITS1 and ITS2 DNA', 'gi|2765599|emb|Z78474.1|PKZ78474 P.kolopakingii 5.8S rRNA gene and ITS1 and ITS2 DNA', 'gi|2765598|emb|Z78473.1|PSZ78473 P.sanderianum 5.8S rRNA gene and ITS1 and ITS2 DNA', 'gi|2765597|emb|Z78472.1|PLZ78472 P.lowii 5.8S rRNA gene and ITS1 and ITS2 DNA', 'gi|2765596|emb|Z78471.1|PDZ78471 P.dianthum 5.8S rRNA gene and ITS1 and ITS2 DNA', 'gi|2765595|emb|Z78470.1|PPZ78470 P.parishii 5.8S rRNA gene and ITS1 and ITS2 DNA', 'gi|2765594|emb|Z78469.1|PHZ78469 P.haynaldianum 5.8S rRNA gene and ITS1 and ITS2 DNA', 'gi|2765593|emb|Z78468.1|PAZ78468 P.adductum 5.8S rRNA gene and ITS1 and ITS2 DNA', 'gi|2765592|emb|Z78467.1|PSZ78467 P.stonei 5.8S rRNA gene and ITS1 and ITS2 DNA', 'gi|2765591|emb|Z78466.1|PPZ78466 P.philippinense 5.8S rRNA gene and ITS1 and ITS2 DNA', 'gi|2765590|emb|Z78465.1|PRZ78465 P.rothschildianum 5.8S rRNA gene and ITS1 and ITS2 DNA', 'gi|2765589|emb|Z78464.1|PGZ78464 P.glanduliferum 5.8S rRNA gene and ITS1 and ITS2 DNA', 'gi|2765588|emb|Z78463.1|PGZ78463 P.glanduliferum 5.8S rRNA gene and ITS1 and ITS2 DNA', 'gi|2765587|emb|Z78462.1|PSZ78462 P.sukhakulii 5.8S rRNA gene and ITS1 and ITS2 DNA', 'gi|2765586|emb|Z78461.1|PWZ78461 P.wardii 5.8S rRNA gene and ITS1 and ITS2 DNA', 'gi|2765585|emb|Z78460.1|PCZ78460 P.ciliolare 5.8S rRNA gene and ITS1 and ITS2 DNA', 'gi|2765584|emb|Z78459.1|PDZ78459 P.dayanum 5.8S rRNA gene and ITS1 and ITS2 DNA', 'gi|2765583|emb|Z78458.1|PHZ78458 P.hennisianum 5.8S rRNA gene and ITS1 and ITS2 DNA', 'gi|2765582|emb|Z78457.1|PCZ78457 P.callosum 5.8S rRNA gene and ITS1 and ITS2 DNA', 'gi|2765581|emb|Z78456.1|PTZ78456 P.tonsum 5.8S rRNA gene and ITS1 and ITS2 DNA', 'gi|2765580|emb|Z78455.1|PJZ78455 P.javanicum 5.8S rRNA gene and ITS1 and ITS2 DNA', 'gi|2765579|emb|Z78454.1|PFZ78454 P.fowliei 5.8S rRNA gene and ITS1 and ITS2 DNA', 'gi|2765578|emb|Z78453.1|PSZ78453 P.schoseri 5.8S rRNA gene and ITS1 and ITS2 DNA', 'gi|2765577|emb|Z78452.1|PBZ78452 P.bougainvilleanum 5.8S rRNA gene and ITS1 and ITS2 DNA', 'gi|2765576|emb|Z78451.1|PHZ78451 P.hookerae 5.8S rRNA gene and ITS1 and ITS2 DNA', 'gi|2765575|emb|Z78450.1|PPZ78450 P.papuanum 5.8S rRNA gene and ITS1 and ITS2 DNA', 'gi|2765574|emb|Z78449.1|PMZ78449 P.mastersianum 5.8S rRNA gene and ITS1 and ITS2 DNA', 'gi|2765573|emb|Z78448.1|PAZ78448 P.argus 5.8S rRNA gene and ITS1 and ITS2 DNA', 'gi|2765572|emb|Z78447.1|PVZ78447 P.venustum 5.8S rRNA gene and ITS1 and ITS2 DNA', 'gi|2765571|emb|Z78446.1|PAZ78446 P.acmodontum 5.8S rRNA gene and ITS1 and ITS2 DNA', 'gi|2765570|emb|Z78445.1|PUZ78445 P.urbanianum 5.8S rRNA gene and ITS1 and ITS2 DNA', 'gi|2765569|emb|Z78444.1|PAZ78444 P.appletonianum 5.8S rRNA gene and ITS1 and ITS2 DNA', 'gi|2765568|emb|Z78443.1|PLZ78443 P.lawrenceanum 5.8S rRNA gene and ITS1 and ITS2 DNA', 'gi|2765567|emb|Z78442.1|PBZ78442 P.bullenianum 5.8S rRNA gene and ITS1 and ITS2 DNA', 'gi|2765566|emb|Z78441.1|PSZ78441 P.superbiens 5.8S rRNA gene and ITS1 and ITS2 DNA', 'gi|2765565|emb|Z78440.1|PPZ78440 P.purpuratum 5.8S rRNA gene and ITS1 and ITS2 DNA', 'gi|2765564|emb|Z78439.1|PBZ78439 P.barbatum 5.8S rRNA gene and ITS1 and ITS2 DNA']}
		s = summarize_contents(os.path.abspath("data/ls_orchid.fasta"))
		self.assertDictEqual(d4, s)

		d5 = {'File:': 'm_cold.fasta', 'Path:': os.path.abspath('data'), 'Num_records:': 1, 'Names:': ['gi|8332116|gb|BE037100.1|BE037100'], 'IDs:': ['gi|8332116|gb|BE037100.1|BE037100'], 'Descriptions': ["gi|8332116|gb|BE037100.1|BE037100 MP14H09 MP Mesembryanthemum crystallinum cDNA 5' similar to cold acclimation protein, mRNA sequence"]}
		s = summarize_contents(os.path.abspath("data/m_cold.fasta"))
		self.assertDictEqual(d5, s)

		d6 = {'File:': 'opuntia.fasta', 'Path:': os.path.abspath('data'), 'Num_records:': 7, 'Names:': ['gi|6273291|gb|AF191665.1|AF191665', 'gi|6273290|gb|AF191664.1|AF191664', 'gi|6273289|gb|AF191663.1|AF191663', 'gi|6273287|gb|AF191661.1|AF191661', 'gi|6273286|gb|AF191660.1|AF191660', 'gi|6273285|gb|AF191659.1|AF191659', 'gi|6273284|gb|AF191658.1|AF191658'], 'IDs:': ['gi|6273291|gb|AF191665.1|AF191665', 'gi|6273290|gb|AF191664.1|AF191664', 'gi|6273289|gb|AF191663.1|AF191663', 'gi|6273287|gb|AF191661.1|AF191661', 'gi|6273286|gb|AF191660.1|AF191660', 'gi|6273285|gb|AF191659.1|AF191659', 'gi|6273284|gb|AF191658.1|AF191658'], 'Descriptions': ['gi|6273291|gb|AF191665.1|AF191665 Opuntia marenae rpl16 gene; chloroplast gene for chloroplast product, partial intron sequence', 'gi|6273290|gb|AF191664.1|AF191664 Opuntia clavata rpl16 gene; chloroplast gene for chloroplast product, partial intron sequence', 'gi|6273289|gb|AF191663.1|AF191663 Opuntia bradtiana rpl16 gene; chloroplast gene for chloroplast product, partial intron sequence', 'gi|6273287|gb|AF191661.1|AF191661 Opuntia kuehnrichiana rpl16 gene; chloroplast gene for chloroplast product, partial intron sequence', 'gi|6273286|gb|AF191660.1|AF191660 Opuntia echinacea rpl16 gene; chloroplast gene for chloroplast product, partial intron sequence', 'gi|6273285|gb|AF191659.1|AF191659 Opuntia pachypus rpl16 gene; chloroplast gene for chloroplast product, partial intron sequence', 'gi|6273284|gb|AF191658.1|AF191658 Opuntia subulata rpl16 gene; chloroplast gene for chloroplast product, partial intron sequence']}
		s = summarize_contents(os.path.abspath("data/opuntia.fasta"))
		self.assertDictEqual(d6, s)
