# Set parameters from a csv file and export to STEP

## Description

Reads data from a .csv file and sets user parameters in the model and then exports the model to STEP. When setting parameters be aware that this sample is setting user parameters. It's also possible to set model parameters but that's not demonstrated here. Also when accessing parameters, it is case sensitive so the names you use in your program much exactly match the names in the model.

## Code Samples

* [Python](#Python)
* [C++](#C++)

|  |
| --- |
| Copy Code |

```
import adsk.core, adsk.fusion, traceback

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui  = app.userInterface

        design = app.activeProduct
        # Read the csv file.
        cnt = 0
        file = open('C://Temp//values.csv')
        for line in file:
            # Get the values from the csv file.
            pieces = line.split(',')

            length = pieces[0]
            width = pieces[1]
            height = pieces[2]

            # Set the parameters.
            lengthParam = design.userParameters.itemByName('Length')
            lengthParam.expression = length

            widthParam = design.userParameters.itemByName('Width')
            widthParam.expression = width

            heightParam = design.userParameters.itemByName('Height')
            heightParam.expression = height

            #Export the STEP file.
            exportMgr = design.exportManager
            stepOptions = exportMgr.createSTEPExportOptions('C:\\Temp\\test_​box' + str(cnt) + '.stp')
            cnt += 1
            res = exportMgr.execute(stepOptions)

        ui.messageBox('Finished')
    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
```

|  |
| --- |
| Copy Code |

```
#include <Core/Application/Application.h>
#include <Core/UserInterface/UserInterface.h>
#include <Fusion/Fusion/UserParameters.h>
#include <Fusion/Fusion/UserParameter.h>
#include <Fusion/Fusion/STEPExportOptions.h>
#include <Fusion/Fusion/ExportManager.h>

#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>

using namespace adsk::core;
using namespace adsk::fusion;

Ptr<UserInterface> ui;

typedef std::vector<std::vector<std::string>> DataSet;

void loadCSVFile(const std::string& csvFilePath, DataSet& dataSet)
{
    std::ifstream infile(csvFilePath);

    while (infile)
    {
        std::string s;
        if (!getline(infile, s))
            break;

        std::istringstream ss(s);
        std::vector<std::string> record;

        while (ss)
        {
            std::string s;
            if (!getline(ss, s, ','))
                break;
            record.push_back(s);
        }

        dataSet.push_back(record);
    }
}

std::string getTempPath()
{
    std::string strTempPath;
#ifdef XI_WIN
    char chPath[MAX_PATH];
    if (::GetTempPathA(MAX_PATH, chPath))
        strTempPath = chPath;
#else  // Mac
    NSString* tempDir = NSTemporaryDirectory();
    if (tempDir == nil)
        tempDir = @"/tmp";
    strTempPath = [tempDir UTF8String];
#endif // XI_WIN
    return strTempPath;
}

extern "C" XI_EXPORT bool run(const char* context)
{
    Ptr<Application> app = Application::get();
    if (!app)
        return false;

    ui = app->userInterface();
    if (!ui)
        return false;

    // Read the csv file.
    int cnt = 0;

     DataSet dataSet;
     loadCSVFile("C:\\Temp\\values.csv", dataSet);

    for (auto data : dataSet)
    {
        // Get the values from the csv file.
        std::string length = data.at(0);
        std::string width = data.at(1);
        std::string height = data.at(2);

        // Set the parameters.
        Ptr<UserParameters> userParams = design->userParameters();
        if (!userParams)
            return false;
        Ptr<UserParameter> lengthParam = userParams->itemByName("Length");
        if (!lengthParam)
            return false;
        lengthParam->expression(length);

        Ptr<UserParameter> widthParam = userParams->itemByName("Width");
        if (!widthParam)
            return false;
        widthParam->expression(width);

        Ptr<UserParameter> heightParam = userParams->itemByName("Height");
        if (!heightParam)
            return false;
        heightParam->expression(height);

        // Export the STEP file.
        Ptr<ExportManager> exportMgr = design->exportManager();
        if (!exportMgr)
            return false;
         std::string filename = "C:\\Temp\\test_box" + std::to_string(cnt) + ".stp";
         Ptr<STEPExportOptions> stepOptions = exportMgr->createSTEPExportOptions(filename);
        if (!stepOptions)
            return false;

        ++cnt;
        exportMgr->execute(stepOptions);
    }

    return true;
}
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |