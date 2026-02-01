# Import Manager API Sample

## Description

Demonstrates how to import different formats to Fusion document

## Code Samples

* [Python](#Python)
* [C++](#C++)

|  |
| --- |
| Copy Code |

```
import adsk.core, adsk.fusion, traceback
import os.path, sys

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui  = app.userInterface

        # Get import manager
        importManager = app.importManager

        # Get iges import options
        igesFileName = 'C:\\APISampleImportNeutralIgs.igs'
        igesOptions = importManager.createIGESImportOptions(igesFileName)

        # Import iges file to new document
        importManager.importToNewDocument(igesOptions)

        # Get sat import options
        satFileName = 'C:\\APISampleImportNeutralSat.sat'
        satOptions = importManager.createSATImportOptions(satFileName)
        satOptions.isViewFit = False

        # Get active design
        product = app.activeProduct
        design = adsk.fusion.Design.cast(product)

        # Get root component
        rootComp = design.rootComponent

        # Import sat file to root component
        importManager.importToTarget(satOptions, rootComp)

        # Get smt import options
        smtFileName = 'C:\\APISampleImportNeutralSmt.smt'
        smtOptions = importManager.createSMTImportOptions(smtFileName)
        smtOptions.isViewFit = False

        # Import smt file to root component
        importManager.importToTarget(smtOptions, rootComp)

        # Get step import options
        stpFileName = 'C:\\APISampleImportNeutralStp.stp'
        stpOptions = importManager.createSTEPImportOptions(stpFileName)
        stpOptions.isViewFit = False

        # Import step file to root component
        importManager.importToTarget(stpOptions, rootComp)

        # Get dxf import options
        #dxfFileName = 'C:\\APISampleImportNeutralDxf2D.dxf'
        dxfOptions = importManager.createDXF2DImportOptions(dxfFileName, rootComp.xZConstructionPlane)
        dxfOptions.isViewFit = False

        # Import dxf file to root component
        importManager.importToTarget(dxfOptions, rootComp)

        dxfOptions = importManager.createDXF2DImportOptions(dxfFileName, rootComp.xZConstructionPlane)
        dxfOptions.isViewFit = False
        # Set the flag true to merge all the layers of DXF into single sketch.
        dxfOptions.isSingleSketchResult = True

        # Import dxf file to root component
        importManager.importToTarget(dxfOptions, rootComp)

        # Get archive import options
        archiveFileName = 'C:\\APISampleImportNeutralF3d2.f3d'
        archiveOptions = importManager.createFusionArchiveImportOptions(archiveFileName)

        # Import archive file to root component
        importManager.importToTarget(archiveOptions, rootComp)

        # Close the new created document
        doc = app.activeDocument
        doc.close(False)
    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
```

|  |
| --- |
| Copy Code |

```
#include <Core/Application/Application.h>
#include <Core/Application/Document.h>
#include <Core/Application/ImportManager.h>
#include <Core/Application/FusionArchiveImportOptions.h>
#include <Core/Application/SATImportOptions.h>
#include <Core/Application/IGESImportOptions.h>
#include <Core/Application/SMTImportOptions.h>
#include <Core/Application/STEPImportOptions.h>
#include <Core/Application/DXF2DImportOptions.h>
#include <Core/UserInterface/UserInterface.h>
#include <Fusion/Fusion/Design.h>
#include <Fusion/Components/Component.h>
#include <Fusion/Construction/ConstructionPlane.h>

using namespace adsk::core;
using namespace adsk::fusion;

Ptr<UserInterface> ui;

extern "C" XI_EXPORT bool run(const char* context)
{
    Ptr<Application> app = Application::get();
    if (!app)
        return false;

    ui = app->userInterface();
    if (!ui)
        return false;

    // Get import manager
    Ptr<ImportManager> importManager = app->importManager();
    if (!importManager)
        return false;

    // Get iges import options
     const std::string igesFileName = "C:\\APISampleImportNeutralIgs.igs";
    Ptr<IGESImportOptions> igesOptions = importManager->createIGESImportOptions(igesFileName);

    // Import iges file to new document
    importManager->importToNewDocument(igesOptions);

    // Get sat import options
     const std::string satFileName = "C:\\APISampleImportNeutralSat.sat";
    Ptr<SATImportOptions> satOptions = importManager->createSATImportOptions(satFileName);
    if (!satOptions)
        return false;
    satOptions->isViewFit(false);

    // Get active design
    Ptr<Design> design = app->activeProduct();
    if (!design)
        return false;

    // Get root component
    Ptr<Component> rootComp = design->rootComponent();

    // Import sat file to root component
    importManager->importToTarget(satOptions, rootComp);

    // Get smt import options
     const std::string smtFileName = "C:\\APISampleImportNeutralSmt.smt";
    Ptr<STEPImportOptions> stpOptions = importManager->createSTEPImportOptions(stpFileName);
    if (!stpOptions)
        return false;
    stpOptions->isViewFit(false);

    // Import step file to root component
    importManager->importToTarget(stpOptions, rootComp);

    // Get dxf import options
     const std::string dxfFileName = "C:\\APISampleImportNeutralDxf2D.dxf";
    Ptr<DXF2DImportOptions> dxfOptions =
        importManager->createDXF2DImportOptions(dxfFileName, rootComp->xZConstructionPlane());
    if (!dxfOptions)
        return false;
    dxfOptions->isViewFit(false);

    // Import dxf file to root component
    importManager->importToTarget(dxfOptions, rootComp);

    Ptr<DXF2DImportOptions> dxfOptions =
        importManager->createDXF2DImportOptions(dxfFileName, rootComp->xZConstructionPlane());
    if (!dxfOptions)
        return false;
    dxfOptions->isViewFit(false);
    // Set the flag true to merge all the layers of DXF into single sketch.
    dxfOptions->isSingleSketchResult(true);

    // Import dxf file to root component
    importManager->importToTarget(dxfOptions, rootComp);

    // Get archive import options
     const std::string archiveFileName = "C:\\APISampleImportNeutralF3d2.f3d";
    Ptr<FusionArchiveImportOptions> archiveOptions = importManager->createFusionArchiveImportOptions(archiveFileName);

    // Import archive file to root component
    importManager->importToTarget(archiveOptions, rootComp);

    // Close the new created document
    Ptr<Document> doc = app->activeDocument();
    if (!doc)
        return false;
    doc->close(false);

    return true;
}
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |