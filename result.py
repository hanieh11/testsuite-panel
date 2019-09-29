import uuid
import datetime

class Result():
    def __init__(self,obj):
        self.final_result = "network"
        self.act = False
        self.getSatusValue(obj)
        self.getKeyValue(obj)
        self.getId()
        self.checkForFormes(obj)
        self.checkForDateTime(obj)
        self.finish()
        
    def getSatusValue(self,obj):
        if obj.ui.statusCheckbox.isChecked() :
            self.final_result = self.final_result + ".rule."
        else:
            self.final_result = self.final_result + ".tmpl."
        test_name = obj.tests.currentText()
        self.final_result = self.final_result + test_name.lower()

    def getKeyValue(self,obj):
        key = obj.ui.resultCombo.currentText()
        if key != "All" :
            self.final_result = self.final_result + "." + str(key)

    def getId(self):
        random_id = uuid.uuid4()
        random_id = random_id.hex[0:6]
        self.final_result = self.final_result + "[id:" + random_id

    def checkForFormes(self,obj):
        self.getTestFormValues(obj.t_form)
        if obj.a_form :
            action_name = obj.actions.currentText()
            if  action_name != "NULL":
                self.act = True
                self.getOtherFormValues(obj.a_form,action_name)
        if obj.ag_form :
            aggregation_name = obj.aggregation.currentText()
            if  aggregation_name != "NULL":
                self.getOtherFormValues(obj.ag_form,aggregation_name)   

    def getTestFormValues(self,form):
            for i in form.properties.keys() :
                item = form.properties.get(i)
                if item.property("type") == "QLineEdit" :
                    value = item.text()
                    if value != "" or self.act :
                        self.final_result = self.final_result + "," + " " + i + ":" + '"' + value + '"'
                elif item.property("type") == "QSpinBox" :
                    value = item.value()
                    if value != 0 or self.act :
                        self.final_result = self.final_result + "," + " " + i + ":" + '"' + str(value) + '"'
                elif item.property("type") == "QCheckBox" :
                    if item.isChecked() or self.act :
                        self.final_result = self.final_result + "," + " " + i + ":" + '"' + str(item.isChecked()) + '"'
                elif item.property("type") == "QComboBox" :
                    value = item.currentText()
                    if value != "" or self.act :
                        self.final_result = self.final_result + "," + " " + i + ":" + '"' + value + '"'

    def getOtherFormValues(self,form,name):
        if form.properties :
            if name == "SCRIPT" : name = "script"
            if name == "SLEEP" : name = "sleep"
            if name == "WEBSERVICE" : name = "service"
            if name == "AVGCOUNT" : name = "avgInCount"
            if name == "AVGTIME" : name = "avgInTime"
            self.final_result = self.final_result + "," + " " + name + ":"
            item = list(form.properties.values())[0]
            if item.property("type") == "QLineEdit" :
                value = item.text()
                self.final_result = self.final_result + '"' + value + '"'
            elif item.property("type") == "QSpinBox" :
                value = item.value()
                self.final_result = self.final_result + '"' + str(value) + '"'

    def checkForDateTime(self,obj):
        today = (datetime.date.today())
        
        from_Qdate = obj.ui.fromDate.date()
        from_Qdate = from_Qdate.toString("yyyy-MM-dd")
        from_date = datetime.date(int(from_Qdate[0:4]),int(from_Qdate[5:7]),int(from_Qdate[8:10]))

        to_Qdate = obj.ui.toDate.date()
        to_Qdate = to_Qdate.toString("yyyy-MM-dd")
        to_date = datetime.date(int(to_Qdate[0:4]),int(to_Qdate[5:7]),int(to_Qdate[8:10]))

        from_Qtime = obj.ui.fromTime.time()
        from_Qtime = from_Qtime.toString("HH:mm")
        from_time = from_Qtime.replace(":","")
        from_time = int(from_time)

        to_Qtime = obj.ui.toTime.time()
        to_Qtime = to_Qtime.toString("HH:mm")
        to_time = to_Qtime.replace(":","")
        to_time = int(to_time)

        if from_date >= today :
            self.final_result = self.final_result + "," + " " + "fromDate:" + '"' + str(from_date) + '"'
        if to_date >= today and to_date >= from_date :
            self.final_result = self.final_result + "," + " " + "toDate:" + '"' + str(to_date) + '"'
        if to_time >= from_time :
            if from_time != 0 :
                self.final_result = self.final_result + "," + " " + "fromTime:" + '"' + from_Qtime + '"'
            if to_time != 2359 :
                self.final_result = self.final_result + "," + " " + "toTime:" + '"' + to_Qtime + '"'

    def finish(self):
        self.final_result = self.final_result + "]"