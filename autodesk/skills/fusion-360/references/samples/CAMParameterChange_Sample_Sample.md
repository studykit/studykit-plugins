# CAM Parameter Modification API Sample

## Description

Demonstrates changing parameters of existing toolpaths.

## Code Samples

* [Python](#Python)
* [C++](#C++)

|  |
| --- |
| Copy Code |

```
import adsk.core, adsk.cam, traceback

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        doc = app.activeDocument
        products = doc.products

        # Get the CAM product
        cam = adsk.cam.CAM.cast(products.itemByProductType("CAMProductType"))

        # List of all setups
        setups = cam.setups

        for setup in setups:
            # Change the program name of each setup to 1234
            programNameParam = setup.parameters.itemByName('job_programName')
            programNameParam.expression = "\'1234\'"

            for operation in setup.operations:
                # Change tolerance in all operations
                toleranceParam = operation.parameters.itemByName('tolerance')
                toleranceParam.expression = "0.1mm"

        # Generate all toolpaths, skipping any that are already valid
        cam.generateAllToolpaths(True)
    except:
        if ui:
            #ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
```

|  |
| --- |
| Copy Code |

```
#include <Core/CoreAll.h>
#include <CAM/CAMAll.h>

using namespace adsk::core;
using namespace adsk::cam;

extern "C" XI_EXPORT bool run(const char* context)
{
    Ptr<Document> doc = Application::get()->activeDocument();
    Ptr<CAM> cam = doc->products()->itemByProductType("CAMProductType");

    // List of CAM setups
    Ptr<Setups> setups = cam->setups();

    for each (Ptr<Setup> setup in setups)
    {
        // Change the program name for each setup
        setup->parameters()->itemByName("job_programName")->expression("\'12345\'");
        for each (Ptr<Operation> operation in setup->allOperations())
        {
            // Change the tolerance of each operation
            operation->parameters()->itemByName("tolerance")->expression("0.1mm");
        }
    }

    // Generate all toolpaths
    cam->generateAllToolpaths(true);

    return true;
}
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |