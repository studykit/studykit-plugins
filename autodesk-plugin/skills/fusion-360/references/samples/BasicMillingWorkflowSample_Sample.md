# Basic Milling Workflow Sample

## Description

Demonstrates the creation of a basic milling workflow from script

Demonstrates creating a setup, searching tool library to retrieve a tool, create a couple of machining operations and a NC program, ready for post processing.

Use the 2D Strategies model from the Fusion CAM Samples folder as your CAD model.

## Code Samples

* [C++](#C++)
* [Python](#Python)

|  |
| --- |
| Copy Code |

```
#include <Core/CoreAll.h>
#include <Fusion/FusionAll.h>
#include <Cam/CamAll.h>
#include <chrono>
#include <thread>
#include <algorithm>

#ifdef _WINDOWS
#include <shlwapi.h>
#else
#include <stdlib.h>
#endif

using namespace adsk::core;
using namespace adsk::fusion;
using namespace adsk::cam;

extern "C" XI_EXPORT bool run(const char* context)
{
    // Initialisation
    Ptr<Application> app = Application::get();
    Ptr<UserInterface> ui = app->userInterface();
    Ptr<Document> doc = nullptr;

    // Load by URN a specific sample project to demonstrate a basic milling workflow.
    std::string urn = "urn:adsk.wipprod:fs.file:vf.KoBHzV4mTOiNvFStiBwpzA?version=1"; // Production

    // Load 2D Strategies model from the Fusion CAM Samples folder
    Ptr<DataFile> sampleFile = app->data()->findFileById(urn);
    if (sampleFile)
    {
        doc = app->documents()->open(sampleFile, true);
    }

    // Did we find our document?
    if (!doc)
    {
        ui->messageBox("Sample file not found, using the current document.", "", MessageBoxButtonTypes::OKButtonType);

        // Use existing document, load 2D Strategies model from the Fusion CAM Samples folder
        doc = app->activeDocument();
    }

    // Switch to manufacturing space
    Ptr<Workspace> camWS = ui->workspaces()->itemById("CAMEnvironment");
    camWS->activate();

    Ptr<Products> products = doc->products();
    if (!products)
        return false;

    // Check if the document has a CAMProductType. It will return if there are no CAM operations in it.
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

    // Find tools in sample tool library

    // Get the tool libraries from the library manager
    Ptr<CAMManager> camManager = CAMManager::get();
    Ptr<CAMLibraryManager> libraryManager = camManager->libraryManager();
    Ptr<ToolLibraries> toolLibraries = libraryManager->toolLibraries();

    // We can use a library URl directly if we know its address (here we use Fusion"s Metric sample library)
    Ptr<URL> toolLibraryUrl = URL::create("systemlibraryroot://Samples/Milling Tools (Metric).json");

    // Load tool library
    Ptr<ToolLibrary> toolLibrary = toolLibraries->toolLibraryAtURL(toolLibraryUrl);
    if (!toolLibrary)
    {
        ui->messageBox("Failed to load tool library");
        return false;
    }

    // Create some variables for the milling tools which will be used in the operations
    Ptr<Tool> faceTool = nullptr;
    Ptr<Tool> adaptiveTool = nullptr;

    // Searching the face mill and the bull nose using a loop for the roughing operations
    for (Ptr<Tool>& tool : toolLibrary)
    {
        // Read the tool type
        Ptr<ChoiceParameterValue> toolTypeParameter = tool->parameters()->itemByName("tool_type")->value();
        std::string toolType = toolTypeParameter->value();

        // Select the first face tool found
        if (toolType == "face mill" && !faceTool)
        {
            faceTool = tool;
        }

        // Search the roughing tool
        else if (toolType == "bull nose end mill" && !adaptiveTool)
        {
            // We look for a bull nose end mill tool larger or equal to 10mm but less than 14mm
            Ptr<FloatParameterValue> diameterParameter = tool->parameters()->itemByName("tool_diameter")->value();
            double diameter = diameterParameter->value();
            if (diameter >= 1.0 && diameter < 1.4)
            {
                adaptiveTool = tool;
            }
        }

        // Exit when the 2 tools are found
        if (faceTool && adaptiveTool)
        {
            break;
        }
    }

    if (!faceTool)
    {
        ui->messageBox("No face mill tool found");
        return false;
    }
    if (!adaptiveTool)
    {
        ui->messageBox("No bull nose end mill tool found");
        return false;
    }

    // Create setup
    Ptr<CAM> cam = products->itemByProductType("CAMProductType");
    Ptr<Setups> setups = cam->setups();
    Ptr<SetupInput> setupInput = setups->createInput(OperationTypes::MillingOperation);

    // Create a list for the models to add to the setup Input
    std::vector<Ptr<Base>> models;
    Ptr<BRepBody> part = cam->designRootOccurrence()->bRepBodies()->item(0);
    if (!part)
    {
        ui->messageBox(
            "No part found in the current document, exiting sample script.", "", MessageBoxButtonTypes::OKButtonType);
        return false;
    }
    // Add the part to the model list
    models.push_back(part);
    // Pass the model list to the setup input
    setupInput->models(models);
    // Create the setup
    Ptr<Setup> setup = setups->add(setupInput);
    // Change some properties of the setup
    setup->name() = "CAM Basic Script Sample";
    setup->stockMode(SetupStockModes::RelativeBoxStock);
    // Set offset mode
    setup->parameters()->itemByName("job_stockOffsetMode")->expression("'simple'");
    // Set offset stock side
    setup->parameters()->itemByName("job_stockOffsetSides")->expression("0 mm");
    // Set offset stock top
    setup->parameters()->itemByName("job_stockOffsetTop")->expression("2 mm");
    // Set setup origin
    Ptr<ChoiceParameterValue> wcs_origin_boxPoint = setup->parameters()->itemByName("wcs_origin_boxPoint")->value();
    wcs_origin_boxPoint->value("top 1");

    // Face operation

    // Create a face operation input
    Ptr<OperationInput> faceInput = setup->operations()->createInput("face");
    faceInput->tool(faceTool);
    faceInput->displayName("Face Operation");
    faceInput->parameters()->itemByName("tolerance")->expression("0.01 mm");
    faceInput->parameters()->itemByName("stepover")->expression("0.75 * tool_diameter");
    faceInput->parameters()
        ->itemByName("direction")
        ->expression("'climb'"); // Must be single quotes inside double quotes

    // Add the operation to the setup
    Ptr<Operation> faceOp = setup->operations()->add(faceInput);

    // Adaptive operation
    Ptr<OperationInput> adaptiveInput = setup->operations()->createInput("adaptive");
    adaptiveInput->tool(adaptiveTool);
    adaptiveInput->displayName("Adaptive Roughing");
    adaptiveInput->parameters()->itemByName("tolerance")->expression("0.1 mm");
    adaptiveInput->parameters()->itemByName("maximumStepdown")->expression("5 mm");
    adaptiveInput->parameters()->itemByName("fineStepdown")->expression("0.25 * maximumStepdown");
    adaptiveInput->parameters()->itemByName("flatAreaMachining")->expression("false");

    // Add the operation to the setup
    Ptr<Operation> adaptiveOp = setup->operations()->add(adaptiveInput);

    // Generate operations
    cam->generateToolpath(faceOp);
    Ptr<GenerateToolpathFuture> genFuture = cam->generateToolpath(adaptiveOp);

    // ncProgram and post-processing

    // Get the post library from library manager
    Ptr<PostLibrary> postLibrary = libraryManager->postLibrary();

    // Query post library to get postprocessor list
    Ptr<PostConfigurationQuery> postQuery = postLibrary->createQuery(LibraryLocations::Fusion360LibraryLocation);
    postQuery->vendor("Autodesk");
    postQuery->capability(PostCapabilities::Milling);
    std::vector<Ptr<PostConfiguration>> postConfigs = postQuery->execute();

    Ptr<URL> importedURL;
    std::string ncExtension;
    // Find the "XYZ" post in the post library and import it to local library
    for (Ptr<PostConfiguration>& config : postConfigs)
    {
        if (config->description() == "XYZ")
        {
            ncExtension = config->extension();
            Ptr<URL> configUrl = URL::create("user://");
            importedURL = postLibrary->importPostConfiguration(config, configUrl, "NCProgramSamplePost.cps");
            break;
        }
    }

    // Get the imported local post config
    Ptr<PostConfiguration> postConfig = postLibrary->postConfigurationAtURL(importedURL);

    // Create NCProgramInput object
    Ptr<NCProgramInput> ncInput = cam->ncPrograms()->createInput();
    ncInput->displayName("NC Program Sample");

    // Change some nc program parameters...
    Ptr<CAMParameters> ncParameters = ncInput->parameters();

    Ptr<StringParameterValue> nc_program_filename = ncParameters->itemByName("nc_program_filename")->value();
    nc_program_filename->value("NCProgramSample");

    Ptr<BooleanParameterValue> nc_program_openInEditor = ncParameters->itemByName("nc_program_openInEditor")->value();
    nc_program_openInEditor->value(true);

    // Set temp directory as output directory
    std::string outputFolder = cam->temporaryFolder();

    // Variable outputFolder may contain backslashes but nc_program_output_folder requires forward slashes
    std::replace_if(
        outputFolder.begin(), outputFolder.end(), [](char ch) { return ch == '\\'; }, '/');

    Ptr<StringParameterValue> nc_program_output_folder = ncParameters->itemByName("nc_program_output_folder")->value();
    nc_program_output_folder->value(outputFolder);

    // Select the operations to generate (we skip steep_and_shallow here)
    ncInput->operations({faceOp, adaptiveOp});

    // Add a new ncprogram from the ncprogram input
    Ptr<NCProgram> newProgram = cam->ncPrograms()->add(ncInput);

    // Set post processor
    newProgram->postConfiguration(postConfig);

    // Change some post parameter
    Ptr<CAMParameters> postParameters = newProgram->postParameters();

    // NcProgram parameters are passed without units to the postprocessor
    Ptr<FloatParameterValue> builtin_tolerance = postParameters->itemByName("builtin_tolerance")->value();
    builtin_tolerance->value(0.01);

    Ptr<FloatParameterValue> builtin_minimumChordLength =
        postParameters->itemByName("builtin_minimumChordLength")->value();
    builtin_minimumChordLength->value(0.33);

    // Update/apply post parameters
    newProgram->updatePostParameters(postParameters);

    // Post-process
    // Set post options, by default post process only valid operations containing toolpath data
    Ptr<NCProgramPostProcessOptions> postOptions = NCProgramPostProcessOptions::create();

    // Ensure toolpaths are visible
    faceOp->isLightBulbOn(true);
    adaptiveOp->isLightBulbOn(true);

    // To avoid errors, post-process only when toolpath generation has completed
    if (!genFuture)
        return false;
    while (!genFuture->isGenerationCompleted())
    {
        std::this_thread::sleep_for(std::chrono::milliseconds(1));
    }
    newProgram->postProcess(postOptions);

    // Advise where the NC file is located to indicate completion
    ui->messageBox(
        "The result has been written to:\n" + outputFolder + "/" + nc_program_filename->value() + ncExtension,
        "Post processing is complete  \t\t\t\t\t");

    return true;
}
```

|  |
| --- |
| Copy Code |

```
import adsk.core, adsk.fusion, adsk.cam, traceback
import time

def run(context):
    ui = None
    try:

        #################### Initialisation #####################
        app = adsk.core.Application.get()
        ui  = app.userInterface

        PROJECT_URN = 'urn:adsk.wipprod:fs.file:vf.KoBHzV4mTOiNvFStiBwpzA?version=1' # Production

        # Load by URN a specific sample project to demonstrate a basic milling workflow.
        doc = loadProjectFromURN(PROJECT_URN)
        if doc is None:
            return

        # Switch to manufacturing space
        camWS: adsk.core.Workspace = ui.workspaces.itemById('CAMEnvironment')
        camWS.activate()

        # Get the CAM product
        products: adsk.core.Products = doc.products

        #################### Find tools in sample tool library ####################
        # Get the tool libraries from the library manager
        camManager = adsk.cam.CAMManager.get()
        libraryManager: adsk.cam.CAMLibraryManager = camManager.libraryManager
        toolLibraries: adsk.cam.ToolLibraries = libraryManager.toolLibraries

        # We can use a library URl directly if we know its address (here we use Fusion's Metric sample library)
        url = adsk.core.URL.create('systemlibraryroot://Samples/Milling Tools (Metric).json')

        # Load tool library
        toolLibrary: adsk.cam.ToolLibrary = toolLibraries.toolLibraryAtURL(url)

        # Create some variables for the milling tools which will be used in the operations
        faceTool: adsk.cam.Tool = None
        adaptiveTool: adsk.cam.Tool = None

        # Searching the face mill and the bull nose using a loop for the roughing operations
        for tool in toolLibrary:
            # Read the tool type
            toolType = tool.parameters.itemByName('tool_type').value.value

            # Select the first face tool found
            if toolType == 'face mill' and not faceTool:
                faceTool = tool

            # Search the roughing tool
            elif toolType == 'bull nose end mill' and not adaptiveTool:
                # We look for a bull nose end mill tool larger or equal to 10mm but less than 14mm
                diameter = tool.parameters.itemByName('tool_diameter').value.value
                if diameter >= 1.0 and diameter < 1.4:
                    adaptiveTool = tool

            # Exit when the 2 tools are found
            if faceTool and adaptiveTool:
                break

        #################### Create setup ####################
        cam: adsk.cam.CAM = adsk.cam.CAM.cast(products.itemByProductType("CAMProductType"))
        setups: adsk.cam.Setups = cam.setups
        setupInput: adsk.cam.SetupInput = setups.createInput(adsk.cam.OperationTypes.MillingOperation)
        # Create a list for the models to add to the setup Input
        models = []

        # Identify the part or exit gracefully
        try:
            part: adsk.fusion.BRepBody = cam.designRootOccurrence.bRepBodies.item(0)
        except Exception as e:
            ui.messageBox('No part found in the current document, exiting sample script.')
            return

        # Add the part to the model list
        models.append(part)
        # Pass the model list to the setup input
        setupInput.models = models
        # Create the setup
        setup: adsk.cam.Setup = setups.add(setupInput)
        # Change some properties of the setup
        setup.name = 'CAM Basic Script Sample'
        setup.stockMode = adsk.cam.SetupStockModes.RelativeBoxStock
        # Set offset mode
        setup.parameters.itemByName('job_stockOffsetMode').expression = "'simple'"
        # Set offset stock side
        setup.parameters.itemByName('job_stockOffsetSides').expression = '0 mm'
        # Set offset stock top
        setup.parameters.itemByName('job_stockOffsetTop').expression = '2 mm'
        # Set setup origin
        setup.parameters.itemByName('wcs_origin_boxPoint').value.value = 'top 1'

        #################### Face operation ####################
        # Create a face operation input
        faceInput: adsk.cam.OperationInput = setup.operations.createInput('face')
        faceInput.tool = faceTool
        faceInput.displayName = 'Face Operation'
        faceInput.parameters.itemByName('tolerance').expression = '0.01 mm'
        faceInput.parameters.itemByName('stepover').expression = '0.75 * tool_diameter'
        faceInput.parameters.itemByName('direction').expression = "'climb'"

        # Add the operation to the setup
        faceOp: adsk.cam.OperationBase = setup.operations.add(faceInput)

        #################### Adaptive operation ####################
        adaptiveInput = setup.operations.createInput('adaptive')
        adaptiveInput.tool = adaptiveTool
        adaptiveInput.displayName = 'Adaptive Roughing'
        adaptiveInput.parameters.itemByName('tolerance').expression = '0.1 mm'
        adaptiveInput.parameters.itemByName('maximumStepdown').expression = '5 mm'
        adaptiveInput.parameters.itemByName('fineStepdown').expression = '0.25 * maximumStepdown'
        adaptiveInput.parameters.itemByName('flatAreaMachining').expression = 'false'

        # Add the operation to the setup
        adaptiveOp: adsk.cam.OperationBase = setup.operations.add(adaptiveInput)

        ##################### Generate operations ####################
        cam.generateToolpath(faceOp)
        genFuture: adsk.cam.GenerateToolpathFuture = cam.generateToolpath(adaptiveOp)

        #################### ncProgram and post-processing ####################
        # Get the post library from library manager
        postLibrary: adsk.cam.PostLibrary = libraryManager.postLibrary

        # Query post library to get postprocessor list
        libraryLocation = adsk.cam.LibraryLocations.Fusion360LibraryLocation
        postQuery: adsk.cam.PostConfigurationQuery = postLibrary.createQuery(libraryLocation)
        postQuery.vendor = "Autodesk"
        postQuery.capability = adsk.cam.PostCapabilities.Milling
        postConfigs: list[adsk.cam.PostConfiguration] = postQuery.execute()

        # Find the "XYZ" post in the post library and import it to local library
        ncExtension = ''
        for config in postConfigs:
            if config.description == 'XYZ':
                ncExtension = config.extension
                url = adsk.core.URL.create("user://")
                importedURL = postLibrary.importPostConfiguration(config, url, "NCProgramSamplePost.cps")

        # Get the imported local post config
        postConfig: adsk.cam.PostConfiguration = postLibrary.postConfigurationAtURL(importedURL)

        # Create NCProgramInput object
        ncInput: adsk.cam.NCProgramInput = cam.ncPrograms.createInput()
        ncInput.displayName = 'NC Program Sample'

        # Change some nc program parameters...
        ncFilename = 'NCProgramSample'
        ncParameters: adsk.cam.CAMParameters = ncInput.parameters
        ncParameters.itemByName('nc_program_filename').value.value = ncFilename
        ncParameters.itemByName('nc_program_openInEditor').value.value = True
        ncParameters.itemByName('nc_program_nc_extension').value.value = ncExtension

        # Set temp directory as output directory
        # Make the path valid for Fusion by replacing \\ to / in the path
        outputFolder = str(cam.temporaryFolder).replace('\\', '/')
        ncParameters.itemByName('nc_program_output_folder').value.value = outputFolder

        # Select the operations to generate
        ncInput.operations = [faceOp, adaptiveOp]

        # Add a new ncprogram from the ncprogram input
        newProgram: adsk.cam.NCProgram = cam.ncPrograms.add(ncInput)

        # Set post processor
        newProgram.postConfiguration = postConfig

        # Change some post parameters
        postParameters: adsk.cam.CAMParameters = newProgram.postParameters

        # NcProgram parameters are passed without units to the postprocessor
        postParameters.itemByName('builtin_tolerance').value.value = 0.01
        postParameters.itemByName('builtin_minimumChordLength').value.value = 0.33

        # Update/apply post parameters
        newProgram.updatePostParameters(postParameters)

        # Post-process
        # Set post options, by default post process only valid operations containing toolpath data
        postOptions = adsk.cam.NCProgramPostProcessOptions.create()

        # Ensure toolpaths are visible
        faceOp.isLightBulbOn = True
        adaptiveOp.isLightBulbOn = True

        # To avoid errors, post-process only when toolpath generation has completed
        while not genFuture.isGenerationCompleted:
            time.sleep(1)
        newProgram.postProcess(postOptions)

        # Advise where the NC file is located to indicate completion
        ui.messageBox(f'The results have been written to:\n{outputFolder}/{ncFilename}{ncExtension}',
                     'Post processing is complete  \t\t\t\t\t'); # Prevent line breaks of the pathname

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))

def loadProjectFromURN(urn:str = None) -> adsk.core.Document:
    ''' Minimal self-contained function to load and return a document via URN or return None safely '''
    doc: adsk.core.Document = None
    app = adsk.core.Application.get()
    if urn is not None:
        try: # File not found causes an exception
            project: adsk.core.DataFile = app.data.findFileById(urn)
            if project:
                doc = app.documents.open(project, True)
            else:
                app.userInterface.messageBox(f'File not found for URN: {urn}!')
        except Exception as e:
            if str(e)[0:38] == '3 : Design is located in another team.':
                # Although the document has been loaded, variable 'doc' may not be populated
                if doc is None:
                    doc: adsk.core.Document = adsk.core.Application.get().activeDocument
            elif str(e)[0:20] == '3 : file not found':
                app.userInterface.messageBox(f'File not found for URN: {urn}!')
            else:
                # Abandon for unhandled errors, displaying the error message.
                app.userInterface.messageBox(f'Failed:{str(e)}\n{traceback.format_exc()}')
    return doc
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |