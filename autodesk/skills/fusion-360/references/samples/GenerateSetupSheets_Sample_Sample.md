# Generate Setup Sheets API Sample

## Description

Demonstrates generating the setup sheets for an existing toolpath..

## Code Samples

* [C++](#C++)
* [Python](#Python)

|  |
| --- |
| Copy Code |

```
#include <Core/CoreAll.h>
#include <CAM/CAMAll.h>

#ifdef _WINDOWS
#include <shlwapi.h>
#else
#include <stdlib.h>
#endif

using namespace adsk::core;
using namespace adsk::cam;

Ptr<UserInterface> ui;

extern "C" XI_EXPORT bool run(const char* context)
{
    Ptr<Application> app = Application::get();
    if (!app)
        return false;

    ui = app->userInterface();
    if (!ui)
        return false;

    Ptr<Document> doc = app->activeDocument();
    if (!doc)
        return false;

    Ptr<Products> products = doc->products();
    if (!products)
        return false;

    Ptr<CAM> camProduct = products->itemByProductType("CAMProductType");
    if (!camProduct)
    {
        ui->messageBox(
            "There are no CAM operations in the active document. This script requires the active document to contain "
            "at least one CAM operation.",
            "No CAM Operations Exist",
            MessageBoxButtonTypes::OKButtonType,
            MessageBoxIconTypes::CriticalIconType);
        return false;
    }

    std::string outputFolder = camProduct->temporaryFolder();
    SetupSheetFormats sheetFormat = SetupSheetFormats::HTMLFormat;
    DialogResults dlgResults = ui->messageBox(
        "View setup sheets when done?",
        "Generate Setup Sheets",
        MessageBoxButtonTypes::YesNoButtonType,
        MessageBoxIconTypes::QuestionIconType);
    bool viewResults = dlgResults == DialogResults::DialogNo ? false : true;

    int scenario = 3;
    switch (scenario)
    {
    case 1:
        {
            ui->messageBox("Setup sheets for all operations will be generated.");
            camProduct->generateAllSetupSheets(sheetFormat, outputFolder, viewResults);
        }
        break;
    case 2:
        {
            ui->messageBox("Setup sheets for operations in the first setup will be generated.");
            Ptr<Setups> setups = camProduct->setups();
            if (!setups)
                return false;

            Ptr<Setup> setup = setups->item(0);
            if (!setup)
                return false;

            camProduct->generateSetupSheet(setup, sheetFormat, outputFolder, viewResults);
        }
        break;
    case 3:
        {
            ui->messageBox("A setup sheet for the first operation in the first setup will be generated.");
            Ptr<Setups> setups = camProduct->setups();
            if (!setups)
                return false;

            Ptr<Setup> setup = setups->item(0);
            if (!setup)
                return false;

            // It is a set of Operations, Folders and Patterns.
            Ptr<ObjectCollection> objects = setup->allOperations();
            if (!objects)
                return false;

            if (objects->count() == 0)
            {
                ui->messageBox("There is not any operation in the first setup!");
                return false;
            }

            Ptr<Base> baseObject = objects->item(0);
            if (!baseObject)
                return false;

            Operation* pOperation = baseObject->query<Operation>();
            if (!pOperation)
                return false;

            Ptr<Operation> operation(pOperation, false);
            if (operation->hasToolpath())
            {
                camProduct->generateSetupSheet(operation, sheetFormat, outputFolder, viewResults);
            }
            else
            {
                ui->messageBox("This operation has no toolpath.  A valid toolpath must exist in order for a setup "
                               "sheet to be generated.");
                return false;
            }
        }
        break;
    default:
        break;
    }

    // Show output folder.
    ui->messageBox("Setup Sheets have been generated in '" + outputFolder + "'.");
#ifdef _WINDOWS
    ShellExecuteA(nullptr, "open", outputFolder.c_str(), nullptr, nullptr, SW_SHOWNORMAL);
#else
    std::string command = "open " + outputFolder;
    system(command.c_str());
#endif

    // Active CAM workspace if it is not the active one.
    if (ui->activeWorkspace()->name() != "CAM")
    {
        DialogResults result = ui->messageBox(
            "Activate the CAM Workspace?",
            "CAM Workspace Activate",
            MessageBoxButtonTypes::YesNoButtonType,
            MessageBoxIconTypes::QuestionIconType);
        bool activeCAMWorkspace = result == DialogResults::DialogYes ? true : false;
        if (activeCAMWorkspace)
        {
            Ptr<Workspace> camWorkspace = ui->workspaces()->itemById("CAMEnvironment");
            camWorkspace->activate();
        }
    }

    return true;
}
```

|  |
| --- |
| Copy Code |

```
# For this sample script to run, the active Fusion document must contain at least one CAM operation.

import adsk.core, adsk.fusion, adsk.cam, traceback, os

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui = app.userInterface
        doc = app.activeDocument
        products = doc.products
        product = products.itemByProductType('CAMProductType')

        # check if the document has a CAMProductType.  It will not if there are no CAM operations in it.
        if not product:
            ui.messageBox('There are no CAM operations in the active document.  This script requires the active document to contain at least one CAM operation.',
                            'No CAM Operations Exist',
                            adsk.core.MessageBoxButtonTypes.OKButtonType,
                            adsk.core.MessageBoxIconTypes.CriticalIconType)
            return

        cam = adsk.cam.CAM.cast(product)

        # specify the output folder and format for the setup sheets
        outputFolder = cam.temporaryFolder
        sheetFormat = adsk.cam.SetupSheetFormats.HTMLFormat
        #sheetFormat = adsk.cam.SetupSheetFormats.ExcelFormat (not currently supported on Mac)

        # prompt the user with an option to view the resulting setup sheets.
        viewResults = ui.messageBox('View setup sheets when done?', 'Generate Setup Sheets',
                                    adsk.core.MessageBoxButtonTypes.YesNoButtonType,
                                    adsk.core.MessageBoxIconTypes.QuestionIconType)
        if viewResults == adsk.core.DialogResults.DialogNo:
            viewResult = False
        else:
            viewResult = True

        # set the value of scenario to 1, 2 or 3 to generate setup sheets for all, for the first setup, or for the first operation of the first setup.
        scenario = 1
        if scenario == 1:
            ui.messageBox('Setup sheets for all operations will be generated.')
            cam.generateAllSetupSheets(sheetFormat, outputFolder, viewResult)
        elif scenario == 2:
            ui.messageBox('Setup sheets for operations in the first setup will be generated.')
            setup = cam.setups.item(0)
            cam.generateSetupSheet(setup, sheetFormat, outputFolder, viewResult)
        elif scenario == 3:
            ui.messageBox('A setup sheet for the first operation in the first setup will be generated.')
            setup = cam.setups.item(0)
            operations = setup.allOperations
            operation = operations.item(0)
            if operation.hasToolpath:
                cam.generateSetupSheet(operation, sheetFormat, outputFolder, viewResult)
            else:
                ui.messageBox('This operation has no toolpath.  A valid toolpath must exist in order for a setup sheet to be generated.')
                return

        ui.messageBox('Setup Sheets have been generated in:\n' + outputFolder)

        # open the output folder in Finder on Mac or in Explorer on Windows
        if (os.name == 'posix'):
            os.system('open "%s"' % outputFolder)
        elif (os.name == 'nt'):
            os.startfile(outputFolder)

        # Prompt user with an option to switch to the CAM workspace if it's not already active
        if ui.activeWorkspace.name != 'CAM':
            activateCAMWorkspace = ui.messageBox('Activate the CAM Workspace?','CAM Workspace Activate',
                                                 adsk.core.MessageBoxButtonTypes.YesNoButtonType,
                                                 adsk.core.MessageBoxIconTypes.QuestionIconType)

            if activateCAMWorkspace == adsk.core.DialogResults.DialogYes:
                workspaces = ui.workspaces
                camWorkspace = workspaces.itemById("CAMEnvironment")
                camWorkspace.activate()

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |