# Material API Sample

## Description

Demonstrates using materials and appearance using the API.

To use the sample, create a new Python or C++ script and copy and paste this code, replacing the default code. The sample also used an external appearance library which you can get [here](../ExtraFiles/APISampleMaterialLibrary2.adsklib). Copy that to any location on your computer and edit the path in the script. When running the script, have a design open that contains a body in the root component.

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
        ui = app.userInterface

        # Load a local material library. You'll need to edit the path to the libary.
        materialLibs = app.materialLibraries
        matLib = materialLibs.load('C:/Temp//APISampleMaterialLibrary2.adsklib')

        # Get the first appearance from the library.
        appear = matLib.appearances.item(0)

        # Copy the appearance into the design.
        des = adsk.fusion.Design.cast(app.activeProduct)
        appear = des.appearances.addByCopy(appear, f'{appear.name}_Copied')

        # Apply the appearance to the first body in the design.
        root = des.rootComponent
        body = root.bRepBodies.item(0)
        body.appearance = appear

        # Unload the library.
        if matLib.isNative == False:
            matLib.unload()
    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
```

|  |
| --- |
| Copy Code |

```
#include <Core/CoreAll.h>
#include <Fusion/FusionAll.h>

using namespace adsk::core;
using namespace adsk::fusion;

Ptr<Application> app;
Ptr<UserInterface> ui;

extern "C" XI_EXPORT bool run(const char* context)
{
    app = Application::get();
    if (!app)
        return false;

    Ptr<Product> product = app->activeProduct();
    if (!product)
        return false;

    Ptr<Design> design = product;
    if (!design)
        return false;

    // Load a local material library. You'll need to edit the path to the  library.
    Ptr<MaterialLibraries> matLibs = app->materialLibraries();
    if (!matLibs)
        return false;

     Ptr<MaterialLibrary> matLib = matLibs->load("C:/Temp/APISampleMaterialLibrary2.adsklib");

    // Get the first appearance from the library.
    Ptr<Appearance> existingAppear = matLib->appearances()->item(0);
    if (!existingAppear)
        return false;

    // Copy the appearance into the design.
    Ptr<Appearance> appear = design->appearances()->addByCopy(existingAppear, existingAppear->name() + "_Copied");

    // Get the first body in the root component of the design.
    Ptr<Component> rootComp = design->rootComponent();
    if (!rootComp)
        return false;

    Ptr<BRepBody> body = rootComp->bRepBodies()->item(0);
    if (!body)
        return false;

    // Apply the appearance to the body.
    body->appearance(appear);

    if (matLib->isNative() == false)
    {
        matLib->unload();
    }

    return true;
}
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |