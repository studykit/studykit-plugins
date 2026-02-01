# Generate Toolpaths API Sample

## Description

Demonstrates generating the toolpaths in the active document.

## Code Samples

* [C++](#C++)
* [Python](#Python)

|  |
| --- |
| Copy Code |

```
#include <Core/CoreAll.h>
#include <CAM/CAMAll.h>

#include <chrono>

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

    // set the value of scenario to 1, 2 or 3 to generate all, the first setup, or the first operation of the first
    // setup.
    int scenario = 1;
    Ptr<GenerateToolpathFuture> future;
    std::string message;
    switch (scenario)
    {
    case 1:
        {
            future = camProduct->generateAllToolpaths(false);
            message = "The toolpaths for all operations in the document have been generated.";
        }
        break;
    case 2:
        {
            Ptr<Setups> setups = camProduct->setups();
            if (!setups)
                return false;

            Ptr<Setup> setup = setups->item(0);
            if (!setup)
                return false;

            future = camProduct->generateToolpath(setup);
            message = "The toolpaths for the operations of the first setup in the document have been generated.";
        }
        break;
    case 3:
        {
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
                ui->messageBox("There are not any operations in the first setup!");
                return false;
            }

            Ptr<Operation> operation = objects->item(0);
            future = camProduct->generateToolpath(operation);
            message = "The toolpath for the first operation of the first setup in the document have been generated.";
        }
        break;
    default:
        break;
    }

    if (!future)
        return false;

    int operationNum = future->numberOfOperations();
    Ptr<ProgressDialog> progressDlg = ui->createProgressDialog();
    progressDlg->isCancelButtonShown(false);
    progressDlg->isBackgroundTranslucent(false);
    progressDlg->show("Toolpath Generation Progress", "Generating Toolpaths", 0, 10);

    // Since toolpaths are calculated in parallel, loop the progress bar while the toolpaths are being generated but
    // none are yet complete.
    while (future->isGenerationCompleted() == false)
    {
        int n = 0;
        std::chrono::time_point<std::chrono::system_clock> startTime = std::chrono::system_clock::now();
        while (future->numberOfCompleted() == 0)
        {
            std::chrono::time_point<std::chrono::system_clock> currentTime = std::chrono::system_clock::now();
            std::chrono::duration<double> elapsed_seconds = currentTime - startTime;
            if (elapsed_seconds.count() > .125)
            {
                startTime = std::chrono::system_clock::now();
                n += 1;
                progressDlg->progressValue(n);
                adsk::doEvents();
            }
            if (n > 10)
                n = 0;
        }

        // Set the progress bar value to the number of completed toolpaths.
        progressDlg->progressValue(future->numberOfCompleted());

        // Set the progress bar max to the number of operations to be completed.
        progressDlg->maximumValue(operationNum);

        // set the message for the progress dialog to track the progress value and the total number of operations to be
        // completed.
        progressDlg->message("Generating %v of %m toolpaths");
        adsk::doEvents();
    }

    progressDlg->hide();

    ui->messageBox(message);

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
import adsk.core, adsk.fusion, traceback, time

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui = app.userInterface

        # Get the CAM product.
        doc = app.activeDocument
        products = doc.products
        product = products.itemByProductType('CAMProductType')
        cam = adsk.cam.CAM.cast(product)
        if not cam:
            ui.messageBox('No CAM data exists in the active document.')
            return

        # Verify that there are any setups.
        if cam.allOperations.count == 0:
            ui.messageBox('No CAM operations exist in the active document.')
            return

        #set the value of scenario to 1, 2 or 3 to generate all, the first setup, or the first operation of the first setup.
        scenario = 1
        if scenario == 1:
            future = cam.generateAllToolpaths(False)
            message = 'The toolpaths for all operations in the document have been generated.'
        elif scenario == 2:
            setup = cam.setups.item(0)
            future = cam.generateToolpath(setup)
            message = 'The toolpaths for the operations of the first setup in the document have been generated.'
        elif scenario == 3:
            setup = cam.setups.item(0)
            operations = setup.operations
            operation = operations.item(0)
            future = cam.generateToolpath(operation)
            message = 'The toolpath for the first operation of the first setup in the document have been generated.'

        numOps = future.numberOfOperations

        #  create and show the progress dialog while the toolpaths are being generated.
        progress = ui.createProgressDialog()
        progress.isCancelButtonShown = False
        progress.show('Toolpath Generation Progress', 'Generating Toolpaths', 0, 10)

        # Enter a loop to wait while the toolpaths are being generated and update
        # the progress dialog.
        while not future.isGenerationCompleted:
            # since toolpaths are calculated in parallel, loop the progress bar while the toolpaths
            # are being generated but none are yet complete.
            n = 0
            start = time.time()
            while future.numberOfCompleted == 0:
                if time.time() - start > .125: # increment the progess value every .125 seconds.
                    start = time.time()
                    n +=1
                    progress.progressValue = n
                    adsk.doEvents()
                if n > 10:
                    n = 0

            # The first toolpath has finished computing so now display better
            # information in the progress dialog.

            # set the progress bar value to the number of completed toolpaths
            progress.progressValue = future.numberOfCompleted

            # set the progress bar max to the number of operations to be completed.
            progress.maximumValue = numOps

            # set the message for the progress dialog to track the progress value and the total number of operations to be completed.
            progress.message = 'Generating %v of %m' + ' Toolpaths'
            adsk.doEvents()

        progress.hide()
        ui.messageBox(message)

        # Prompt user with an option to switch to the CAM workspace if it's not already active
        if ui.activeWorkspace.id != 'CAMEnvironment':
            dialogResult = ui.messageBox('Activate the CAM Workspace?','CAM Workspace Activate',
                                                 adsk.core.MessageBoxButtonTypes.YesNoButtonType,
                                                 adsk.core.MessageBoxIconTypes.QuestionIconType)

            if dialogResult == adsk.core.DialogResults.DialogYes:
                ws = ui.workspaces.itemById('CAMEnvironment')
                ws.activate()
    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |