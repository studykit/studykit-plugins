# Create CAM Operation From Template API Sample

## Description

Demonstrates adding a new toolpath into the document using an existing CAM template. You can view the template [here](../ExtraFiles/face.f3dhsm-template), although it will be loaded automatically. Run the sample script within any Fusion project containing at least one setup. A new facing operation will be created at the end of each setup discovered.

## Code Samples

* [C++](#C++)
* [Python](#Python)

|  |
| --- |
| Copy Code |

```
// Apply a CAM Template to a specific machining operation on the selected model of each setup.

#include <Core/CoreAll.h>
#include <Fusion/FusionAll.h>
#include <Cam/CamAll.h>
#include <fstream>
#include <algorithm>

using namespace adsk::core;
using namespace adsk::fusion;
using namespace adsk::cam;

// The location from where a sample template file can be downloaded if performed manually.
std::string TEMPLATE_URL = "https://help.autodesk.com/cloudhelp/ENU/Fusion-360-API/ExtraFiles/face.f3dhsm-template";

// The name of the template file.
std::string TEMPLATE_FILE = "face.f3dhsm-template";

// The URN is the identifier of the template as located within Fusion's library of sample templates.
std::string TEMPLATE_URN = "urn:adsk.wipprod:fs.file:vf.p0C9h2KARa61iM_vsZauog?version=1";

// Variable initialisation.
Ptr<Application> app = Application::get();
Ptr<UserInterface> ui = app->userInterface();
Ptr<Document> doc = app->activeDocument();

// Abandon the script with a dialog explaining the reason and solution
bool abandonScript(std::string& notice)
{
    notice += "\nAfter completing the above tasks, run this script again.";
    // Spaces appended to the title make the messageBox wider, preventing line wrapping.
    ui->messageBox(
        notice,
        "Please take note of the following:\t\t\t\t",
        MessageBoxButtonTypes::OKButtonType,
        MessageBoxIconTypes::WarningIconType);
    return true;
}

// Function to check whether the template file exists.
bool fileExists(const std::string& filename)
{
    std::ifstream file(filename);
    return file.good();
}

extern "C" XI_EXPORT bool run(const char* context)
{
    std::string notice = "";
    size_t occurrenceCount = 0;
    size_t bRepBodyCount = 0;

    // Switch to manufacturing space.
    Ptr<Workspace> camWS = ui->workspaces()->itemById("CAMEnvironment");
    camWS->activate();

    // Get the CAM product.
    Ptr<Products> products = doc->products();
    Ptr<Product> product = app->activeProduct();
    Ptr<CAM> cam = products->itemByProductType("CAMProductType");

    // Get the CAD product.
    Ptr<Design> design = products->itemByProductType("DesignProductType");

    // An alternative possibility.
    if (!design)
    {
        Ptr<Design> design = products->itemByProductType("WorkingModelProduct");
    }

    // Check that a model exists in this document.
    if (design)
    {
        occurrenceCount = design->rootComponent()->occurrences()->count();
        bRepBodyCount = design->rootComponent()->bRepBodies()->count();
    }
    else
    {
        notice += "No active Fusion design found.\n";
    }

    if (bRepBodyCount < 1 && occurrenceCount < 1)
    {
        notice += "\nNo model found. Open a Fusion document that contains a model.\n";
    }

    // Check we have an existing setup and abandon if not.
    Ptr<Setups> setups = cam->setups();
    if (setups->count() < 1)
    {
        notice += "\nNo setup found. Create a setup and assign a model to it.\n";
    }

    // Present a single messageBox stating problems, remedies and instructions.
    if (notice.length() > 0)
    {
        return abandonScript(notice);
    }

    // We are unable to read the content of a CAMTemplate dataFile directly from its URN.
    // Instead we download the dataFile from the URN into a temporary folder and read the file contents.

    // Set CAM temporary folder as inputFolder.
    std::string inputFolder = cam->temporaryFolder();

    // Variable inputFolder may contain backslashes but we need forward slashes.
    std::replace_if(
        inputFolder.begin(), inputFolder.end(), [](char ch) { return ch == '\\'; }, '/');

    // Specify the full filename of the template.
    std::string templatePathname = inputFolder + "/" + TEMPLATE_FILE;

    // Check if the template exists(from the path specified above).Show an error if it fails to download.
    if (!fileExists(templatePathname))
    {
        Ptr<DataFile> templateDataFile = app->data()->findFileById(TEMPLATE_URN);
        bool downloadSuccess = false;

        if (templateDataFile)
        {
            downloadSuccess = templateDataFile->download(templatePathname, NULL);
        }
        else
        {
            notice += "\nUnable to locate template via " + TEMPLATE_URN + "\n";
        }

        if (!downloadSuccess)
        {
            // We should never get here but if so, explain how to perform the previous step manually.
            notice += "\nThe template file: " + TEMPLATE_FILE + " has not been found.\n";
            notice += "\nCreate your own template file called \"" + TEMPLATE_FILE;
            notice += "\" or download a sample file from here : \n\n" + TEMPLATE_URL + "\n\n";
            notice += "Move the downloaded template file to this folder:\n\n" + inputFolder + "\n\n";
        }
    }

    // Present a single messageBox stating problems, remedies and instructions.
    if (notice.length() > 0)
    {
        return abandonScript(notice);
    }

    // Iterate through each setup and insert the template into the setup.
    // for each (Ptr<Setup> setup in cam->setups()) // for each iterator fails on Mac when tried.
    for (size_t i = 0; i < setups->count(); i++)
    {
        // Add the template to each setup.
        Ptr<ObjectCollection> results = setups->item(i)->createFromTemplate(templatePathname);

        // Get the operation that was created.What's created will vary depending on what's defined
        // in the template so you may need more logic to find the result you want.
        Ptr<Operation> operation = results->item(0);

        std::string name = operation->name() + " (API added operation)";
        operation->name(name);
    }

    // Generate all toolpaths, skipping any that are already valid.
    cam->generateAllToolpaths(true);

    // Indicate what has changed within the setup.
    notice = "Expand the setup to see all operations.\n\n";
    notice += "Note the operation names appended with: (API added operation).";
    ui->messageBox(
        notice,
        "Operation creation from template complete.\t\t",
        MessageBoxButtonTypes::OKButtonType,
        MessageBoxIconTypes::InformationIconType);

    return true;
}
```

|  |
| --- |
| Copy Code |

```
# Apply a CAM Template to a specific machining operation on the selected model of each setup.

import adsk.core, adsk.fusion, adsk.cam, os, traceback

# The location from where a sample template file can be downloaded if performed manually.
TEMPLATE_URL = 'https://help.autodesk.com/cloudhelp/ENU/Fusion-360-API/ExtraFiles/face.f3dhsm-template'

# The name of the template file.
TEMPLATE_FILE = 'face.f3dhsm-template'

# The URN is the identifier of the template as located within Fusion's library of sample templates.
TEMPLATE_URN = 'urn:adsk.wipprod:fs.file:vf.p0C9h2KARa61iM_vsZauog?version=1'

# Variable initialisation.
app = adsk.core.Application.get()
ui = app.userInterface
doc = app.activeDocument

def abandonScript(notice:str):
    notice += '\nAfter completing the above tasks, run this script again.'
    # Spaces appended to the title make the messageBox wider, preventing line wrapping.
    ui.messageBox(
        notice,
        'Please take note of the following:\t\t\t\t',
        adsk.core.MessageBoxButtonTypes.OKButtonType,
        adsk.core.MessageBoxIconTypes.WarningIconType)

def run(context):

    # Variable initialisation.
    notice = ''
    occurrenceCount = 0
    bRepBodyCount = 0

    try:
        # Switch to manufacturing space.
        camWS = ui.workspaces.itemById('CAMEnvironment')
        camWS.activate()

        # Get the CAM product.
        products = doc.products
        cam: adsk.cam.CAM = products.itemByProductType('CAMProductType')

        # Get the CAD product.
        design: adsk.fusion.Design = products.itemByProductType('DesignProductType')

        # An alternative possibility.
        if not design:
            design = products.itemByProductType('WorkingModelProductType')

        # Check that a model exists in this document.
        if design:
            occurrenceCount  = design.rootComponent.occurrences.count
            bRepBodyCount = design.rootComponent.bRepBodies.count
        else:
            notice += 'No active Fusion design found.\n'

        if bRepBodyCount < 1 and occurrenceCount < 1:
            notice += f'\nNo model found. Open a Fusion document that contains a model.\n'

        # Check we have an existing setup and abandon if not.
        setups: adsk.cam.Setups = cam.setups
        if setups.count < 1:
            notice += '\nNo setup found. Create a setup and assign a model to it.\n'

        # Present a single messageBox stating problems, remedies and instructions.
        if (len(notice) > 0):
            abandonScript(notice)
            return

        # We are unable to read the content of a CAMTemplate dataFile directly from its URN.
        # Instead we download the dataFile from the URN into a temporary folder and read the file contents.

        # Set CAM temporary folder as inputFolder.
        # Variable inputFolder may contain backslashes but we need forward slashes.
        inputFolder = str(cam.temporaryFolder).replace('\\', '/')

        # Specify the full filename of the template.
        templatePathname = f'{inputFolder}/{TEMPLATE_FILE}'

        # Check if the template exists (from the path specified above). Show an error if it fails to download.
        if not os.path.exists(templatePathname):
            templateDataFile: adsk.core.DataFile = None
            try:
                templateDataFile = app.data.findFileById(TEMPLATE_URN)
            except:
                notice += f'\nUnable to locate template via {TEMPLATE_URN}.\n'

            downloadSuccess:bool = False
            if templateDataFile:
                try:
                    downloadSuccess = templateDataFile.download(templatePathname, None)
                except Exception as e:
                    notice += f'\n{e}\n'

            if not downloadSuccess:
                # We should never get here but if so, explain how to perform the previous step manually.
                notice += f'\nThe template file: {TEMPLATE_FILE} has not been found.\n'
                notice += f'\nCreate your own template file called {TEMPLATE_FILE} '
                notice += f'or download a sample file from here:\n\n{TEMPLATE_URL}\n\n'
                notice += f'Move the downloaded template file to this folder:\n\n{inputFolder}\n\n'

        # Present a single messageBox stating problems, remedies and instructions.
        if len(notice) > 0:
            abandonScript(notice)
            return

        # Go through each setup in the document.
        for setup in setups:
            # Add a templated operation to each setup.
            templateInput = adsk.cam.CreateFromCAMTemplateInput.create()
            camTemplate = adsk.cam.CAMTemplate.createFromFile(templatePathname)
            templateInput.camTemplate = camTemplate
            results: list[adsk.cam.OperationBase] = setup.createFromCAMTemplate2(templateInput)

            # Get the operation that was created. What's created will vary depending on what's defined
            # in the template so you may need more logic to find the result you want.
            operation: adsk.cam.OperationBase = results[0]

            # Change the operation name.
            name = operation.name + ' (API added operation)'
            operation.name = name

            # Make the toolpath visible.
            operation.isSuppressed = False
            operation.isLightBulbOn = True

        # Generate all toolpaths, skipping any that are already valid.
        cam.generateAllToolpaths(True)

        # Indicate what has changed within the setup.
        notice = 'Expand the setup to see all operations.\n\n'
        notice += 'Note the operation names appended with: (API added operation).'
        ui.messageBox(
            notice,
            'Operation creation from template complete.\t\t',
            adsk.core.MessageBoxButtonTypes.OKButtonType,
            adsk.core.MessageBoxIconTypes.InformationIconType)

    # Capture and highlight any reason for error
    except Exception as e:
        if ui:
            ui.messageBox(
                f'Failed: {e}\n{format(traceback.format_exc())}',
                'Unable to continue',
                adsk.core.MessageBoxButtonTypes.OKButtonType,
                adsk.core.MessageBoxIconTypes.CriticalIconType)
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |