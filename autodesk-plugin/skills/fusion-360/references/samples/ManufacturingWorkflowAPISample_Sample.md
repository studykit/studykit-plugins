# Manufacturing Workflow API Sample

## Description

Manufacturing Workflow API Sample

This sample script starts by creating a simple component which is then used to describe a milling workflow. It creates a setup, a few operations, pick some tools from a Fusion sample tool library using loops and queries and ends up post-processing the operations out using an NC Program.

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
#include <algorithm>

using namespace adsk::core;
using namespace adsk::fusion;
using namespace adsk::cam;

// Constants used in the script
// We assume we are cutting Aluminum here...

// Milling tool library to get tools from
const std::string MILLING_TOOL_LIBRARY = "Milling Tools (Metric)";

// Material properties for feed and speed calculation
const int ALUMINUM_CUTTING_SPEED = 300;     // mm/min
const double ALUMINUM_FEED_PER_TOOTH = 0.1; // mm/tooth

// Tool preset names (which we know exists for the selected tools)
const std::string ALUMINUM_PRESET_ROUGHING = "alu* rou*";
const std::string ALUMINUM_PRESET_FINISHING = "Aluminum - Finishing";

// Tool types used in this script
const std::string BULL_NOSE_END_MILL = "bull nose end mill";
const std::string BALL_END_MILL = "ball end mill";
const std::string FACE_MILL = "face mill";

// Setup work coordinate system (WCS) location
const std::string TOP_CENTER = "top center";
const std::string TOP_XMIN_YMIN = "top 1";
const std::string TOP_XMAX_YMIN = "top 2";
const std::string TOP_XMIN_YMAX = "top 3";
const std::string TOP_XMAX_YMAX = "top 4";
const std::string TOP_SIDE_YMIN = "top side 1";
const std::string TOP_SIDE_XMAX = "top side 2";
const std::string TOP_SIDE_YMAX = "top side 3";
const std::string TOP_SIDE_XMIN = "top side 4";
const std::string CENTER = "center";
const std::string MIDDLE_XMIN_YMIN = "middle 1";
const std::string MIDDLE_XMAX_YMIN = "middle 2";
const std::string MIDDLE_XMIN_YMAX = "middle 3";
const std::string MIDDLE_XMAX_YMAX = "middle 4";
const std::string MIDDLE_SIDE_YMIN = "middle side 1";
const std::string MIDDLE_SIDE_XMAX = "middle side 2";
const std::string MIDDLE_SIDE_YMAX = "middle side 3";
const std::string MIDDLE_SIDE_XMIN = "middle side 4";
const std::string BOTTOM_CENTER = "bottom center";
const std::string BOTTOM_XMIN_YMIN = "bottom 1";
const std::string BOTTOM_XMAX_YMIN = "bottom 2";
const std::string BOTTOM_XMIN_YMAX = "bottom 3";
const std::string BOTTOM_XMAX_YMAX = "bottom 4";
const std::string BOTTOM_SIDE_YMIN = "bottom side 1";
const std::string BOTTOM_SIDE_XMAX = "bottom side 2";
const std::string BOTTOM_SIDE_YMAX = "bottom side 3";
const std::string BOTTOM_SIDE_XMIN = "bottom side 4";

const double PI = 3.14159265358979323846;

std::vector<std::string> getLibrariesURLs(Ptr<ToolLibraries> libraries, Ptr<URL> url);
std::vector<Ptr<Tool>> getToolsFromLibraryByTypeDiameterRangeAndMinFluteLength(
    Ptr<ToolLibrary> toolLibrary,
    std::string tooltype,
    double minDiameter,
    double maxDiameter,
    double minimumFluteLength = 0.0);
Ptr<BRepBody> createSamplePart(Ptr<Design> design);

extern "C" XI_EXPORT bool run(const char* context)
{
    // Initialisation
    Ptr<Application> app = Application::get();
    Ptr<UserInterface> ui = app->userInterface();

    // Create a new empty document
    Ptr<Document> doc = app->documents()->add(DocumentTypes::FusionDesignDocumentType);

    // Get the design document used to create the sample part
    Ptr<Design> design = app->activeProduct();

    // Switch to manufacturing space
    Ptr<Workspace> camWS = ui->workspaces()->itemById("CAMEnvironment");
    camWS->activate();

    // Get the CAM product
    Ptr<Products> products = doc->products();

    // Create sample part
    Ptr<BRepBody> part = createSamplePart(design);

    // Select cutting tools
    // Get the tool libraries from the library manager
    Ptr<CAMManager> camManager = CAMManager::get();
    Ptr<CAMLibraryManager> libraryManager = camManager->libraryManager();
    Ptr<ToolLibraries> toolLibraries = libraryManager->toolLibraries();

    Ptr<URL> url;
    const bool useHardCodedUrl = false;
    if (useHardCodedUrl)
    {
        // We can use a library URl directly if we know its address
        std::string libUrl = "systemlibraryroot://Samples/Milling Tools (Metric).json";
        url = URL::create(libUrl);
    }
    else
    {
        // Or we can use the tool library objects fusion folder in the tool library
        Ptr<URL> fusionFolder = toolLibraries->urlByLocation(LibraryLocations::Fusion360LibraryLocation);
        std::vector<std::string> fusionLibs = getLibrariesURLs(toolLibraries, fusionFolder);

        // Search the required library url in the libraries
        for (std::string& libUrl : fusionLibs)
        {
            if (libUrl.find(MILLING_TOOL_LIBRARY) != std::string::npos)
            {
                url = URL::create(libUrl);
                break;
            }
        }
    }

    // Load the tool library
    Ptr<ToolLibrary> toolLibrary = toolLibraries->toolLibraryAtURL(url);
    if (!toolLibrary)
    {
        ui->messageBox("Failed to load tool library");
        return false;
    }

    // Create variables to host the milling tools to be used in the operations
    Ptr<Tool> faceTool;
    Ptr<Tool> adaptiveTool;
    Ptr<Tool> finishingTool;

    // Search for the face mill and the bull nose using a loop for the roughing operations
    for (Ptr<Tool> tool : toolLibrary)
    {
        // Read the tool type
        Ptr<ChoiceParameterValue> toolTypeParameter = tool->parameters()->itemByName("tool_type")->value();
        std::string toolType = toolTypeParameter->value();

        if (toolType == FACE_MILL && !faceTool)
        {
            // Select the first face tool found
            faceTool = tool;
        }
        else if (toolType == BULL_NOSE_END_MILL && !adaptiveTool)
        {
            // Search the roughing tool
            // We look for a bull nose end mill tool larger or equal to 12mm but less than 14mm
            Ptr<FloatParameterValue> diameterParameter = tool->parameters()->itemByName("tool_diameter")->value();
            double diameter = diameterParameter->value();
            if (diameter >= 1.2 && diameter < 1.4)
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

    // Using a query, search for a ball end mill tool having diameter between 6 mm and 10 mm and a minimum flute length
    // of 20.001mm
    std::vector<Ptr<Tool>> finishingTools =
        getToolsFromLibraryByTypeDiameterRangeAndMinFluteLength(toolLibrary, BALL_END_MILL, 0.6, 1, 2.0001);

    // For this example, we select the first tool found as our finishing tool
    if (finishingTools.size() == 0)
    {
        ui->messageBox("No ball end mill tool found");
        return false;
    }
    finishingTool = finishingTools[0];

    // Create a setup
    Ptr<CAM> cam = products->itemByProductType("CAMProductType");
    Ptr<Setups> setups = cam->setups();
    Ptr<SetupInput> setupInput = setups->createInput(OperationTypes::MillingOperation);
    // Create a list for the models to add to the setup Input
    std::vector<Ptr<Base>> models;
    // Add the part to the model list
    models.push_back(part);
    // Pass the model list to the setup input
    setupInput->models(models);
    // Create the setup and set some properties
    Ptr<Setup> setup = setups->add(setupInput);
    setup->name("CAM Automation Script Sample");
    setup->stockMode(SetupStockModes::RelativeBoxStock);
    // Set the offset mode
    setup->parameters()->itemByName("job_stockOffsetMode")->expression("\"simple\"");
    // Set the offset stock side
    setup->parameters()->itemByName("job_stockOffsetSides")->expression("0 mm");
    // Set the offset stock top
    setup->parameters()->itemByName("job_stockOffsetTop")->expression("1 mm");
    // Set the setup origin
    Ptr<ChoiceParameterValue> wcs_origin = setup->parameters()->itemByName("wcs_origin_boxPoint")->value();
    wcs_origin->value(TOP_XMIN_YMIN);

    // Face operations
    // Calculate the feed and speed for the face operation
    Ptr<FloatParameterValue> toolDiameterParameter = faceTool->parameters()->itemByName("tool_diameter")->value();
    double toolDiameter = toolDiameterParameter->value(); // cm
    Ptr<IntegerParameterValue> numberOfFlutesParameter =
        faceTool->parameters()->itemByName("tool_numberOfFlutes")->value();
    int numberOfFlutes = numberOfFlutesParameter->value();                            // int
    double spindleSpeed = ALUMINUM_CUTTING_SPEED / PI / (toolDiameter * 10) * 1000;   // rpm
    double cuttingFeedrate = spindleSpeed * ALUMINUM_FEED_PER_TOOTH * numberOfFlutes; // mm/min

    // Create a preset with those calculated feeds
    Ptr<ToolPreset> facePreset = faceTool->presets()->add();
    facePreset->name("Aluminum (set by script)");
    Ptr<FloatParameterValue> tool_spindleSpeed = facePreset->parameters()->itemByName("tool_spindleSpeed")->value();
    tool_spindleSpeed->value(int(spindleSpeed));
    facePreset->parameters()
        ->itemByName("tool_feedCutting")
        ->expression(std::to_string(int(cuttingFeedrate)) + " mm/min");

    // Create a face operation input
    Ptr<OperationInput> input = setup->operations()->createInput("face");
    input->tool(faceTool);
    input->toolPreset(facePreset); // Assign created preset
    input->displayName("Face Operation");
    input->parameters()->itemByName("tolerance")->expression("0.01 mm");
    input->parameters()->itemByName("stepover")->expression("0.75 * tool_diameter");
    input->parameters()->itemByName("direction")->expression("\"climb\"");

    // Determine the pass angle along the largest part dimension
    // Get the stock box dimensions in cm
    Ptr<FloatParameterValue> stockXParameter = setup->parameters()->itemByName("job_stockInfoDimensionX")->value();
    double stockX = stockXParameter->value();
    Ptr<FloatParameterValue> stockYParameter = setup->parameters()->itemByName("job_stockInfoDimensionY")->value();
    double stockY = stockYParameter->value();
    // Determine the pass angle to be along the largest length (X or Y) of the block
    if (stockX >= stockY)
    {
        input->parameters()->itemByName("passAngle")->expression("0 deg");
    }
    else
    {
        input->parameters()->itemByName("passAngle")->expression("90 deg");
    }

    // Add the operation to the setup
    Ptr<OperationBase> faceOp = setup->operations()->add(input);

    // Adaptive operations
    input = setup->operations()->createInput("adaptive");
    input->tool(adaptiveTool);
    input->displayName("Adaptive Roughing");
    input->parameters()->itemByName("tolerance")->expression("0.1 mm");
    input->parameters()->itemByName("maximumStepdown")->expression("5 mm");
    input->parameters()->itemByName("fineStepdown")->expression("0.25 * maximumStepdown");
    input->parameters()->itemByName("flatAreaMachining")->expression("false");

    // Look for a tool preset related to aluminum roughing
    std::vector<Ptr<ToolPreset>> presets = adaptiveTool->presets()->itemsByName(ALUMINUM_PRESET_ROUGHING);
    if (presets.size() > 0)
    {
        // We select and use the first preset found
        Ptr<ToolPreset> adaptivePreset = presets[0];
        input->toolPreset(adaptivePreset);
    }

    // Add the operation to the setup
    Ptr<OperationBase> adaptiveOp = setup->operations()->add(input);

    // Finishing tool preset
    // Get a tool preset from the finishing tool
    Ptr<ToolPreset> finishingPreset;
    presets = finishingTool->presets()->itemsByName(ALUMINUM_PRESET_FINISHING);
    if (presets.size() > 0)
    {
        // Use the first aluminum finishing preset found
        finishingPreset = presets[0];
    }

    // Parallel operations
    input = setup->operations()->createInput("parallel");
    input->tool(finishingTool);
    input->displayName("Parallel Finishing");
    input->parameters()->itemByName("tolerance")->expression("0.01 mm");
    input->parameters()->itemByName("cuspHeightStepover")->expression("0.005 mm");
    input->parameters()->itemByName("boundaryMode")->expression("\"selection\"");
    if (finishingPreset)
    {
        // Assign the finishig tool preset
        input->toolPreset(finishingPreset);
    }

    // Add the operation to the setup
    Ptr<OperationBase> parallelOp = setup->operations()->add(input);

    // Use a contour for the sake of demonstration
    Ptr<BRepEdge> limitEdge;
    for (Ptr<BRepEdge> e : part->edges())
    {
        // This is the inner one: intersection of a plane and a sphere making up a circle
        if (e->geometry()->curveType() == Curve3DTypes::Circle3DCurveType)
        {
            limitEdge = e;
            break;
        }
    }

    if (limitEdge)
    {
        // Apply the limits edge to the operation
        Ptr<CadContours2dParameterValue> cadcontours2dParam =
            parallelOp->parameters()->itemByName("machiningBoundarySel")->value();
        Ptr<CurveSelections> chains = cadcontours2dParam->getCurveSelections();
        Ptr<ChainSelection> chain = chains->createNewChainSelection();
        chain->inputGeometry({limitEdge});
        cadcontours2dParam->applyCurveSelections(chains);
    }

    // Steep and shallow operations
    // Create a folder for finishing operations that require Machining Extension
    Ptr<OperationInput> operationInput = setup->operations()->createInput("folder");
    operationInput->displayName("Machining Extension Required");
    Ptr<CAMFolder> folder = setup->operations()->add(operationInput);

    // Create a steep and shallow operation in the folder
    input = setup->operations()->createInput("steep_and_shallow");
    input->tool(finishingTool);
    input->displayName("Steep and Shallow Finishing");
    input->parameters()->itemByName("tolerance")->expression("0.01 mm");
    input->parameters()->itemByName("useAvoidFlats")->expression("true");
    input->parameters()->itemByName("cuspHeightStepdown")->expression("0.005 mm");
    input->parameters()->itemByName("cuspHeightStepover")->expression("cuspHeightStepdown");
    input->parameters()->itemByName("spiral")->expression("true");
    input->parameters()->itemByName("shallowSpiral")->expression("true");
    input->parameters()->itemByName("offsetSmoothing")->expression("true");
    if (finishingPreset)
    {
        // Assign the finishig tool preset
        input->toolPreset(finishingPreset);
    }

    // Add the operation to the folder
    Ptr<OperationBase> steepAndShallowOp = folder->operations()->add(input);

    // Check whether this toolpath is generatable ("steep_and_shallow" required the manufacturing extension)
    bool isSteepAndShallowGeneratable = false;
    for (Ptr<OperationStrategy> op : setup->operations()->compatibleStrategies())
    {
        if (op->name() == "steep_and_shallow")
        {
            if (op->isGenerationAllowed())
            {
                // isGenerationAllowed will be false if the extension is not active thus preventing the
                // steep_and_shallow operation
                isSteepAndShallowGeneratable = true;
            }
            break;
        }
    }

    // Generate operations
    // List the valid operations to generate
    Ptr<ObjectCollection> operations = ObjectCollection::create();
    operations->add(faceOp);
    operations->add(adaptiveOp);
    operations->add(parallelOp);
    if (isSteepAndShallowGeneratable)
    {
        operations->add(steepAndShallowOp);
    }

    // Create progress bar
    Ptr<ProgressDialog> progressDialog = ui->createProgressDialog();
    progressDialog->isCancelButtonShown(false);
    progressDialog->show("Generating operations->()..", "%p%", 0, 100);
    adsk::doEvents(); // Allow Fusion to update so that the progressDialog updates nicely

    // Generate the valid operations
    Ptr<GenerateToolpathFuture> gtf = cam->generateToolpath(operations);

    // Wait for the generation to be finished and update the progress bar
    while (!gtf->isGenerationCompleted())
    {
        // Calculate progress and update the progress bar
        int total = gtf->numberOfOperations();
        int completed = gtf->numberOfCompleted();
        int progress = int(completed * 100 / total);
        progressDialog->progressValue(progress);
        adsk::doEvents(); // Allow Fusion to update so that the screen does not freeze
    }

    // Generation done
    progressDialog->progressValue(100);
    progressDialog->hide();

    // NC Program and post-processing
    // Get the post library from the library manager
    Ptr<PostLibrary> postLibrary = libraryManager->postLibrary();

    // Query the post library to get the postprocessor list
    Ptr<PostConfigurationQuery> postQuery = postLibrary->createQuery(LibraryLocations::Fusion360LibraryLocation);
    postQuery->vendor("Autodesk");
    postQuery->capability(PostCapabilities::Milling);
    std::vector<Ptr<PostConfiguration>> postConfigs = postQuery->execute();

    // Find the "XYZ" post in the post library and import it to the local library
    Ptr<URL> importedURL;
    for (Ptr<PostConfiguration> config : postConfigs)
    {
        if (config->description() == "XYZ")
        {
            Ptr<URL> _url = URL::create("user://");
            importedURL = postLibrary->importPostConfiguration(config, _url, "NCProgramSamplePost.cps");
        }
    }

    // Get the imported local post config
    Ptr<PostConfiguration> postConfig = postLibrary->postConfigurationAtURL(importedURL);

    // Create the NCProgramInput object
    Ptr<NCProgramInput> ncInput = cam->ncPrograms()->createInput();
    ncInput->displayName("NC Program Sample");

    // Change some nc program parameters...
    Ptr<CAMParameters> ncParameters = ncInput->parameters();
    std::string programName = "NCProgramSample";
    Ptr<StringParameterValue> nc_program_filename = ncParameters->itemByName("nc_program_filename")->value();
    nc_program_filename->value(programName);
    Ptr<BooleanParameterValue> nc_program_openInEditor = ncParameters->itemByName("nc_program_openInEditor")->value();
    nc_program_openInEditor->value(true);

    // Set the temporary directory as the output directory
    std::string outputFolder = cam->temporaryFolder();
    Ptr<StringParameterValue> nc_program_output_folder = ncParameters->itemByName("nc_program_output_folder")->value();
    nc_program_output_folder->value(outputFolder);

    // Select the operations to generate (we skip steep_and_shallow here)
    ncInput->operations({faceOp, adaptiveOp, parallelOp});

    // Add a new ncprogram from the ncprogram input
    Ptr<NCProgram> newProgram = cam->ncPrograms()->add(ncInput);

    // Set the post processor
    newProgram->postConfiguration(postConfig);

    // Change some of the post parameters
    Ptr<CAMParameters> postParameters = newProgram->postParameters();
    Ptr<FloatParameterValue> builtin_tolerance = postParameters->itemByName("builtin_tolerance")->value();
    builtin_tolerance->value(0.02); // NcProgram parameter is passed unchanged to the postprocessor (it has no units)
    Ptr<FloatParameterValue> builtin_minimumChordLength =
        postParameters->itemByName("builtin_minimumChordLength")->value();
    builtin_minimumChordLength->value(0.33); // NcProgram parameter is passed unchanged (it has no units)

    // Update/apply post parameters
    newProgram->updatePostParameters(postParameters);

    // Set post options, by default post process only valid operations containing toolpath data
    Ptr<NCProgramPostProcessOptions> postOptions = NCProgramPostProcessOptions::create();
    // postOptions.PostProcessExecutionBehaviors =
    // adsk.cam.PostProcessExecutionBehaviors.PostProcessExecutionBehavior_PostAll

    // Post-process
    newProgram->postProcess(postOptions);

    // Show the output file
    ui->messageBox(
        "Post processing is complete. The results have been written to:\n" + outputFolder + "/" + programName + ".csv");

    return true;
}

// Return the list of libraries' URLs for the specified libraries
std::vector<std::string> getLibrariesURLs(Ptr<ToolLibraries> libraries, Ptr<URL> url)
{
    std::vector<std::string> urls;
    std::vector<Ptr<URL>> libs = libraries->childAssetURLs(url);
    for (auto& elem : libs)
    {
        urls.push_back(elem->toString());
    }
    for (Ptr<URL> folder : libraries->childFolderURLs(url))
    {
        std::vector<std::string> folderUrls = getLibrariesURLs(libraries, folder);
        urls.insert(urls.end(), folderUrls.begin(), folderUrls.end());
    }
    return urls;
}

//  Return a list of tools that fits the search
std::vector<Ptr<Tool>> getToolsFromLibraryByTypeDiameterRangeAndMinFluteLength(
    Ptr<ToolLibrary> toolLibrary,
    std::string tooltype,
    double minDiameter,
    double maxDiameter,
    double minimumFluteLength)
{
    Ptr<ToolQuery> query = toolLibrary->createQuery();
    // Set the search critera
    query->criteria()->add("tool_type", ValueInput::createByString(tooltype));
    query->criteria()->add("tool_diameter.min", ValueInput::createByReal(minDiameter));
    query->criteria()->add("tool_diameter.max", ValueInput::createByReal(maxDiameter));
    if (minimumFluteLength)
    {
        query->criteria()->add("tool_fluteLength.min", ValueInput::createByReal(minimumFluteLength));
    }
    // Get query results
    std::vector<Ptr<ToolQueryResult>> results = query->execute();
    // Get the tools from the query
    std::vector<Ptr<Tool>> tools;
    // Results have a tool, url, toollibrary and the index of the tool in that library: we just return the tool here
    for (auto& elem : results)
    {
        tools.push_back(elem->tool());
    }
    return tools;
}

// CAD creation functions
Ptr<BRepBody> createBox(Ptr<Design> design, double sizeX, double sizeY, double sizeZ);
Ptr<BRepBody> createSphere(Ptr<Design> design, double radius);
Ptr<BRepBody> getBodyFromBooleanOperation(Ptr<Design> design, Ptr<BRepBody> body1, Ptr<BRepBody> body2);

// Create the sample part for this script
Ptr<BRepBody> createSamplePart(Ptr<Design> design)
{

    // The sample part is a box containing a concave side generated by subtracting the intersection from a sphere.
    // The lower face of the box is at Z = 0 and we position the sphere above but intersecting with the box upper face.
    // Fusion's default behaviour is now to ground the first component of an assembly to the parent.
    // This can be overriden, see Preferences->General->Design->Assemblies->First component grounded to parent.
    // However if we make the first component the box, we can move the sphere without changing anything.

    Ptr<BRepBody> box = createBox(design, 22, 15, 5);
    Ptr<BRepBody> sphere = createSphere(design, 7.5);

    // Get the root component
    Ptr<Component> rootComp = design->rootComponent();
    Ptr<Occurrences> occs = rootComp->occurrences();

    // Get the second Occurrence(sphere) as the first occurrence(box) may be grounded to the parent
    Ptr<Occurrence> occ = occs->item(1);
    Ptr<Matrix3D> mat = occ->transform();

    // Matrix translation, moving the sphere up by 10 units along Z axis
    Ptr<Vector3D> origin = Vector3D::create(0, 0, 10);
    mat->translation(origin);

    // Set the transform
    occ->transform(mat);

    // Snapshot - Determining the position is important!!!
    design->snapshots()->add();

    // Cut the sphere / box intersection from the box to leave a concave face
    Ptr<BRepBody> part = getBodyFromBooleanOperation(design, box, sphere);
    return part;
}

// Create a sample box
Ptr<BRepBody> createBox(Ptr<Design> design, double sizeX, double sizeY, double sizeZ)
{
    Ptr<Component> component = design->rootComponent();
    // Create a sketch
    Ptr<Sketches> sketches = component->sketches();
    Ptr<Sketch> sketch = sketches->add(component->xYConstructionPlane());
    Ptr<SketchLines> lines = sketch->sketchCurves()->sketchLines();
    Ptr<SketchLineList> recLines = lines->addTwoPointRectangle(
        Point3D::create(-sizeX / 2, -sizeY / 2, 0), Point3D::create(sizeX / 2, sizeY / 2, 0));
    Ptr<Profile> prof = sketch->profiles()->item(0);
    Ptr<ExtrudeFeatures> extrudes = component->features()->extrudeFeatures();
    Ptr<ValueInput> distance = ValueInput::createByReal(sizeZ);
    Ptr<ExtrudeFeature> ext = extrudes->addSimple(prof, distance, FeatureOperations::NewComponentFeatureOperation);
    return ext->bodies()->item(0);
}

// Create a sample sphere
Ptr<BRepBody> createSphere(Ptr<Design> design, double radius)
{
    Ptr<Component> component = design->rootComponent();
    // Create a new sketch on the xy plane
    Ptr<Sketches> sketches = component->sketches();
    Ptr<ConstructionPlane> xyPlane = component->xYConstructionPlane();
    Ptr<Sketch> sketch = sketches->add(component->xYConstructionPlane());
    // Draw a circle
    Ptr<SketchCircles> circles = sketch->sketchCurves()->sketchCircles();
    Ptr<SketchCircle> circle = circles->addByCenterRadius(Point3D::create(0, 0, 0), radius);
    // Draw a line to use as the axis of revolution
    Ptr<SketchLines> lines = sketch->sketchCurves()->sketchLines();
    Ptr<SketchLine> axisLine = lines->addByTwoPoints(Point3D::create(-radius, 0, 0), Point3D::create(radius, 0, 0));
    // Get the profile defined by half of the circle
    Ptr<Profile> prof = sketch->profiles()->item(0);
    // Create an revolution input to be able to define the input needed for a revolution
    // while specifying the profile and that a new component is to be created
    Ptr<RevolveFeatures> revolves = component->features()->revolveFeatures();
    Ptr<RevolveFeatureInput> revInput =
        revolves->createInput(prof, axisLine, FeatureOperations::NewComponentFeatureOperation);
    // Define that the extent is an angle of 2*pi to get a sphere
    Ptr<ValueInput> angle = ValueInput::createByReal(2 * PI);
    revInput->setAngleExtent(false, angle);
    // Create the extrusion
    Ptr<RevolveFeature> ext = revolves->add(revInput);

    return ext->bodies()->item(0);
}

// Creates a boolean operation between two bodies
Ptr<BRepBody> getBodyFromBooleanOperation(Ptr<Design> design, Ptr<BRepBody> body1, Ptr<BRepBody> body2)
{
    Ptr<Component> model = design->activeComponent();
    Ptr<Features> features = model->features();
    Ptr<ObjectCollection> bodyCollection = ObjectCollection::create();
    bodyCollection->add(body2);
    Ptr<CombineFeatures> combineFeatures = features->combineFeatures();
    Ptr<CombineFeatureInput> combineFeatureInput = combineFeatures->createInput(body1, bodyCollection);
    combineFeatureInput->operation(FeatureOperations(1));
    combineFeatureInput->isKeepToolBodies(false);
    combineFeatureInput->isNewComponent(false);
    Ptr<CombineFeature> returnValue = combineFeatures->add(combineFeatureInput);
    Ptr<BRepBody> part = returnValue->bodies()->item(0);
    return part;
}
```

|  |
| --- |
| Copy Code |

```
import math, os, traceback
from enum import Enum
import adsk.fusion, adsk.core, adsk.cam

#################### Script Constants ####################
# We assume we are cutting Aluminum here...

# Milling tool library to get tools from
MILLING_TOOL_LIBRARY = 'Milling Tools (Metric)'

# Some material properties for feed and speed calculation
ALUMINUM_CUTTING_SPEED = 300  # mm/min
ALUMINUM_FEED_PER_TOOTH = 0.1 # mm/tooth

# Some tool preset names, known to exist for the selected tools
ALUMINUM_PRESET_ROUGHING = 'alu* rou*'
ALUMINUM_PRESET_FINISHING = 'Aluminum - Finishing'

#################### Useful Enumerators ####################
# Some tool types used in this script (enumerator)
class ToolType(Enum):
    BULL_NOSE_END_MILL = 'bull nose end mill'
    BALL_END_MILL = 'ball end mill'
    FACE_MILL = 'face mill'

# Setup work coordinate system (WCS) location (enumerator)
class SetupWCSPoint(Enum):
    TOP_CENTER = 'top center'
    TOP_XMIN_YMIN = 'top 1'
    TOP_XMAX_YMIN = 'top 2'
    TOP_XMIN_YMAX = 'top 3'
    TOP_XMAX_YMAX = 'top 4'
    TOP_SIDE_YMIN = 'top side 1'
    TOP_SIDE_XMAX = 'top side 2'
    TOP_SIDE_YMAX = 'top side 3'
    TOP_SIDE_XMIN = 'top side 4'
    CENTER = 'center'
    MIDDLE_XMIN_YMIN = 'middle 1'
    MIDDLE_XMAX_YMIN = 'middle 2'
    MIDDLE_XMIN_YMAX = 'middle 3'
    MIDDLE_XMAX_YMAX = 'middle 4'
    MIDDLE_SIDE_YMIN = 'middle side 1'
    MIDDLE_SIDE_XMAX = 'middle side 2'
    MIDDLE_SIDE_YMAX = 'middle side 3'
    MIDDLE_SIDE_XMIN = 'middle side 4'
    BOTTOM_CENTER = 'bottom center'
    BOTTOM_XMIN_YMIN = 'bottom 1'
    BOTTOM_XMAX_YMIN = 'bottom 2'
    BOTTOM_XMIN_YMAX = 'bottom 3'
    BOTTOM_XMAX_YMAX = 'bottom 4'
    BOTTOM_SIDE_YMIN = 'bottom side 1'
    BOTTOM_SIDE_XMAX = 'bottom side 2'
    BOTTOM_SIDE_YMAX = 'bottom side 3'
    BOTTOM_SIDE_XMIN = 'bottom side 4'

#################### Script Entry Point ####################
def run(context) -> None:
    ui = None
    try:

        #################### Initialisation #####################
        app = adsk.core.Application.get()
        ui: adsk.core.UserInterface  = app.userInterface

        # Create a new empty document
        doc: adsk.core.Document = app.documents.add(adsk.core.DocumentTypes.FusionDesignDocumentType)

        # Get the design document used to create the sample part
        design: adsk.core.Product = app.activeProduct

        # Switch to manufacturing space
        camWS: adsk.core.Workspace = ui.workspaces.itemById('CAMEnvironment')
        camWS.activate()

        # Get the CAM product
        products: adsk.core.Products = doc.products

        #################### Create Sample Part ####################

        part: adsk.fusion.BRepBody = createSamplePart(design)

        #################### Select Cutting Tools ####################

        # Get the tool libraries from the library manager
        camManager = adsk.cam.CAMManager.get()
        libraryManager: adsk.cam.CAMLibraryManager = camManager.libraryManager
        toolLibraries: adsk.cam.ToolLibraries = libraryManager.toolLibraries

        url: adsk.core.URL = None
        libUrl = None
        useHardCodedUrl: bool = False
        if useHardCodedUrl:
            # We could use a library URl directly if we know its address ...
            libUrl = 'systemlibraryroot://Samples/Milling Tools (Metric).json'
            url = adsk.core.URL.create(libUrl)

        else:
            # ... or we can use the tool library objects
            # Fusion folder in the tool library
            fusionFolder: adsk.core.URL = toolLibraries.urlByLocation(adsk.cam.LibraryLocations.Fusion360LibraryLocation)
            fusionLibs: list[str] = getLibrariesURLs(toolLibraries, fusionFolder)

            # Search the required library url in the libraries
            for libUrl in fusionLibs:
                if MILLING_TOOL_LIBRARY in libUrl:
                    url = adsk.core.URL.create(libUrl)
                    break

        # Load the tool library
        toolLibrary: adsk.cam.ToolLibrary = toolLibraries.toolLibraryAtURL(url)

        # Create some variables to host the milling tools which will be used in the operations
        faceTool: adsk.cam.Tool = None
        adaptiveTool: adsk.cam.Tool = None
        finishingTool: adsk.cam.Tool = None

        # For the roughing operations, search for the face mill and the bull nose using a loop
        for tool in toolLibrary:
            # Read the tool type
            toolType: adsk.cam.ToolType = tool.parameters.itemByName('tool_type').value.value

            # Select the first face tool found
            if toolType == ToolType.FACE_MILL.value and not faceTool:
                faceTool = tool

            # Search for the roughing tool
            elif toolType == ToolType.BULL_NOSE_END_MILL.value and not adaptiveTool:
                # Look for a bull nose end mill tool larger or equal to 12mm but less than 14mm
                diameter: float = tool.parameters.itemByName('tool_diameter').value.value
                if diameter >= 1.2 and diameter < 1.4:
                    adaptiveTool = tool

            # Exit when the 2 tools are found
            if faceTool and adaptiveTool:
                break

        # Using a query, search for a ball end mill tool with diameter between 6 mm and 10 mm with a minimum flute length of 20.001mm
        finishingTools: list[adsk.cam.Tool] = getToolsFromLibraryByTypeDiameterRangeAndMinFluteLength(toolLibrary, ToolType.BALL_END_MILL.value, 0.6, 1, 2.0001)

        # For this example, we select the first tool found as our finishing tool
        finishingTool = finishingTools[0]

        #################### Create Setup ####################
        cam = adsk.cam.CAM.cast(products.itemByProductType("CAMProductType"))
        setups: adsk.cam.Setups = cam.setups
        setupInput: adsk.cam.SetupInput = setups.createInput(adsk.cam.OperationTypes.MillingOperation)
        # Create a list for the models to add to the setup Input
        models:list = []
        # Add the part to the model list
        models.append(part)
        # Pass the model list to the setup input
        setupInput.models = models
        # Create the setup and set some properties
        setup: adsk.cam.Setup = setups.add(setupInput)
        setup.name = 'CAM Automation Script Sample'
        setup.stockMode = adsk.cam.SetupStockModes.RelativeBoxStock
        # Set the offset mode
        setup.parameters.itemByName('job_stockOffsetMode').expression = "'simple'"
        # Set offset stock side
        setup.parameters.itemByName('job_stockOffsetSides').expression = '0 mm'
        # Set offset stock top
        setup.parameters.itemByName('job_stockOffsetTop').expression = '1 mm'
        # Set setup origin
        setup.parameters.itemByName('wcs_origin_boxPoint').value.value = SetupWCSPoint.TOP_XMIN_YMIN.value

        #################### Face Operations ####################
        # Calculate feed and speed for the face operation
        toolDiameter: float = faceTool.parameters.itemByName('tool_diameter').value.value          # cm
        numberOfFlutes = faceTool.parameters.itemByName('tool_numberOfFlutes').value.value         # int
        spindleSpeed: float = ALUMINUM_CUTTING_SPEED / math.pi / (toolDiameter * 10) * 1000        # rpm
        cuttingFeedrate: float = spindleSpeed * ALUMINUM_FEED_PER_TOOTH * numberOfFlutes           # mm/min

        # Create a preset with those calculated feeds
        facePreset: adsk.cam.ToolPreset = faceTool.presets.add()
        facePreset.name = 'Aluminum (set by script)'
        facePreset.parameters.itemByName('tool_spindleSpeed').value.value = int(spindleSpeed)
        facePreset.parameters.itemByName('tool_feedCutting').expression = str(int(cuttingFeedrate)) + ' mm/min'

        # Create a face operation input
        input: adsk.cam.OperationInput = setup.operations.createInput('face')
        input.tool = faceTool
        input.toolPreset = facePreset # Assign created preset
        input.displayName = 'Face Operation'
        input.parameters.itemByName('tolerance').expression = '0.01 mm'
        input.parameters.itemByName('stepover').expression = '0.75 * tool_diameter'
        input.parameters.itemByName('direction').expression = "'climb'"

        # Determine pass angle along largest part dimension
        # Get stock box dimensions in cm
        stockX: float = setup.parameters.itemByName('job_stockInfoDimensionX').value.value
        stockY: float = setup.parameters.itemByName('job_stockInfoDimensionY').value.value

        # Determine pass angle to be along largest length (X or Y) of the block
        if stockX >= stockY:
            input.parameters.itemByName('passAngle').expression = '0 deg'
        else:
            input.parameters.itemByName('passAngle').expression = '90 deg'

        # Add the operation to the setup
        faceOp: adsk.cam.OperationBase = setup.operations.add(input)

        #################### Adaptive Operations ####################
        input = setup.operations.createInput('adaptive')
        input.tool = adaptiveTool
        input.displayName = 'Adaptive Roughing'
        input.parameters.itemByName('tolerance').expression = '0.1 mm'
        input.parameters.itemByName('maximumStepdown').expression = '5 mm'
        input.parameters.itemByName('fineStepdown').expression = '0.25 * maximumStepdown'
        input.parameters.itemByName('flatAreaMachining').expression = 'false'

        # Check if there is a tool preset related to aluminum roughing
        presets: adsk.cam.ToolPresets = adaptiveTool.presets.itemsByName(ALUMINUM_PRESET_ROUGHING)
        if len(presets) > 0:
            # Select the first preset found
            adaptivePreset: adsk.cam.ToolPreset = presets[0]
            input.toolPreset = adaptivePreset

        # Add the operation to the setup
        adaptiveOp: adsk.cam.OperationBase = setup.operations.add(input)

        #################### Finishing Tool Preset ####################
        # Select a tool preset from the finishing tool
        finishingPreset: adsk.cam.ToolPreset = None
        presets = finishingTool.presets.itemsByName(ALUMINUM_PRESET_FINISHING)
        if len(presets) > 0:
            # Use the first aluminum finishing preset found
            finishingPreset = presets[0]

        #################### Parallel Operations ####################
        input = setup.operations.createInput('parallel')
        input.tool = finishingTool
        input.displayName = 'Parallel Finishing'
        input.parameters.itemByName('tolerance').expression = '0.01 mm'
        input.parameters.itemByName('cuspHeightStepover').expression = '0.005 mm'
        input.parameters.itemByName('boundaryMode').expression = "'selection'"
        if finishingPreset:
            # Assign the finishing tool preset
            input.toolPreset = finishingPreset

        # Add the operation to the setup
        parallelOp: adsk.cam.OperationBase = setup.operations.add(input)

        # Lets use a contour for the sake of demonstration
        limitEdge: adsk.fusion.BRepEdge = None
        for e in part.edges:
            # This is the inner one: intersection of a plane and a sphere making up a circle
            if e.geometry.curveType == adsk.core.Curve3DTypes.Circle3DCurveType:
                limitEdge = e
                break

        if limitEdge:
            # Apply the limiting edge to the operation
            cadcontours2dParam: adsk.cam.CadContours2dParameterValue = parallelOp.parameters.itemByName('machiningBoundarySel').value
            chains: adsk.cam.CurveSelections = cadcontours2dParam.getCurveSelections()
            chain: adsk.cam.ChainSelection = chains.createNewChainSelection()
            chain.inputGeometry = [limitEdge]
            cadcontours2dParam.applyCurveSelections(chains)

        #################### Steep And Shallow Operations ####################
        # Create folder for finishing operations that require Machining Extension
        operationInput: adsk.cam.OperationInput = setup.operations.createInput('folder')
        operationInput.displayName = 'Machining Extension Required'
        folder: adsk.cam.CAMFolder = setup.operations.add(operationInput)

        # Create steep and shallow operation in the folder
        input = setup.operations.createInput('steep_and_shallow')
        input.tool = finishingTool
        input.displayName = 'Steep and Shallow Finishing'
        input.parameters.itemByName('tolerance').expression = '0.01 mm'
        input.parameters.itemByName('useAvoidFlats').expression = 'true'
        input.parameters.itemByName('cuspHeightStepdown').expression = '0.005 mm'
        input.parameters.itemByName('cuspHeightStepover').expression = 'cuspHeightStepdown'
        input.parameters.itemByName('spiral').expression = 'true'
        input.parameters.itemByName('shallowSpiral').expression = 'true'
        input.parameters.itemByName('offsetSmoothing').expression = 'true'

        # Assign the finishing tool preset
        if finishingPreset:
            input.toolPreset = finishingPreset

        # Add the operation to the folder
        steepAndShallowOp: adsk.cam.OperationBase = folder.operations.add(input)

        # Check if this toolpath is generatable as "steep_and_shallow" requires the manufacturing extension
        isSteepAndShallowGeneratable: bool = False
        for op in setup.operations.compatibleStrategies:
            if op.name == 'steep_and_shallow':
                if op.isGenerationAllowed:
                    # If isGenerationAllowed is False, the extension isn't active, preventing generation of the steep_and_shallow operation
                    isSteepAndShallowGeneratable = True
                break

        #################### Generate Operations ####################
        # Include the valid operations to generate
        operations = adsk.core.ObjectCollection.create()
        operations.add(faceOp)
        operations.add(adaptiveOp)
        operations.add(parallelOp)
        if isSteepAndShallowGeneratable:
            operations.add(steepAndShallowOp)

        # create progress bar
        progressDialog: adsk.core.ProgressDialog = ui.createProgressDialog()
        progressDialog.isCancelButtonShown = False
        progressDialog.show('Generating operations...', '%p%', 0, 100)
        adsk.doEvents() # Allow Fusion to update so the progressDialog shows up nicely

        # Generate the valid operations
        gtf: adsk.cam.GenerateToolpathFuture = cam.generateToolpath(operations)

        # Wait for the generation to be finished and update progress bar
        while not gtf.isGenerationCompleted:
            # Calculate progress and update progress bar
            total = gtf.numberOfOperations
            completed = gtf.numberOfCompleted
            progress = int(completed * 100 / total)
            progressDialog.progressValue = progress
            adsk.doEvents() # Allow Fusion to update so the screen doesn't freeze

        # Generation done
        progressDialog.progressValue = 100
        progressDialog.hide()

        #################### NC Program And Post-processing ####################
        # Get the post library from library manager
        postLibrary: adsk.cam.PostLibrary = libraryManager.postLibrary

        # Query post library to get postprocessor list
        postQuery: adsk.cam.PostConfigurationQuery = postLibrary.createQuery(adsk.cam.LibraryLocations.Fusion360LibraryLocation)
        postQuery.vendor = "Autodesk"
        postQuery.capability = adsk.cam.PostCapabilities.Milling
        postConfigs: list[adsk.cam.PostConfiguration] = postQuery.execute()

        # Find the "XYZ" post in the post library and import it to local library
        for config in postConfigs:
            if config.description == 'XYZ':
                url = adsk.core.URL.create("user://")
                importedURL: adsk.core.URL = postLibrary.importPostConfiguration(config, url, "NCProgramSamplePost.cps")

        # Get the imported local post config
        postConfig: adsk.cam.PostConfiguration = postLibrary.postConfigurationAtURL(importedURL)

        # Create NCProgramInput object
        ncInput: adsk.cam.NCProgramInput = cam.ncPrograms.createInput()
        ncInput.displayName = 'NC Program Sample'

        # Change some nc program parameters...
        ncParameters: adsk.cam.CAMParameters = ncInput.parameters
        ncParameters.itemByName('nc_program_filename').value.value = 'NCProgramSample'
        ncParameters.itemByName('nc_program_openInEditor').value.value = True

        # Set user desktop as output directory (Windows and Mac)
        # Make the path valid for Fusion by replacing \\ to / in the path
        desktopDirectory = os.path.expanduser("~/Desktop").replace('\\', '/')
        ncParameters.itemByName('nc_program_output_folder').value.value = desktopDirectory

        # Select the operations to generate (we skip steep_and_shallow here)
        ncInput.operations = [faceOp, adaptiveOp, parallelOp]

        # Add a new ncprogram from the ncprogram input
        newProgram: adsk.cam.NCProgram = cam.ncPrograms.add(ncInput)

        # Set post processor
        newProgram.postConfiguration = postConfig

        # Change some post parameter
        postParameters: adsk.cam.CAMParameters = newProgram.postParameters

        # NcProgram parameters are passed as theyare to the postprocessor (they have no units)
        postParameters.itemByName('builtin_tolerance').value.value = 0.01
        postParameters.itemByName('builtin_minimumChordLength').value.value = 0.33

        # Update/apply post parameters
        newProgram.updatePostParameters(postParameters)

        # Set post options, by default post process only valid operations containing toolpath data
        postOptions = adsk.cam.NCProgramPostProcessOptions.create()

        # Post-process
        newProgram.postProcess(postOptions)

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))

#################### Functions To Make Our Life Easier ####################

def getLibrariesURLs(libraries: adsk.cam.ToolLibraries, url: adsk.core.URL) -> list[str]:
    ''' Return the list of libraries' URLs for the specified libraries '''
    urls: list[str] = []
    libs: list[adsk.core.URL] = libraries.childAssetURLs(url)
    for lib in libs:
        urls.append(lib.toString())
    for folder in libraries.childFolderURLs(url):
        urls = urls + getLibrariesURLs(libraries, folder)
    return urls

def getToolsFromLibraryByTypeDiameterRangeAndMinFluteLength(toolLibrary: adsk.cam.ToolLibrary, tooltype: str, minDiameter: float, maxDiameter: float, minimumFluteLength: float = None) -> list[adsk.cam.Tool]:
    ''' Return a list of tools that satisfy the search '''
    query: adsk.cam.ToolQuery = toolLibrary.createQuery()
    # Set the search critera
    query.criteria.add('tool_type', adsk.core.ValueInput.createByString(tooltype))
    query.criteria.add('tool_diameter.min', adsk.core.ValueInput.createByReal(minDiameter))
    query.criteria.add('tool_diameter.max', adsk.core.ValueInput.createByReal(maxDiameter))
    if minimumFluteLength:
        query.criteria.add('tool_fluteLength.min', adsk.core.ValueInput.createByReal(minimumFluteLength))
    # Get query results
    results: list[adsk.cam.ToolQueryResult] = query.execute()
    # Get the tools from the query
    tools: list[adsk.cam.Tool] = []
    for result in results:
        # Results have a tool, url, toollibrary and the index of the tool in that library: we just return the tool here
        tools.append(result.tool)
    return tools

#################### CAD Creation ####################

def createSamplePart(design: adsk.fusion.Design) -> adsk.fusion.BRepBody:
    """ Creates the sample part for this script """
    # The sample part is a box containing a concave side generated by subtracting the intersection from a sphere.
    # The lower face of the box is at Z=0 and we position the sphere above but intersecting with the box upper face.
    # Fusion's default behaviour is now to ground the first component of an assembly to the parent.
    # This can be overriden, see Preferences ->General ->Design ->Assemblies ->First component grounded to parent
    # However if we make the first component the box, we can move the sphere without changing anything

    box: adsk.fusion.BRepBody = createBox(design, 22, 15, 5) # 1st component occurrence
    sphere: adsk.fusion.BRepBody = createSphere(design, 7.5) # 2nd component occurrence

    # Get the root component
    rootComp: adsk.fusion.Component = design.rootComponent
    occs: adsk.fusion.Occurrences = rootComp.occurrences

    # Get the second Occurrence (sphere) as the first occurrence (box) may be grounded to the parent
    occ: adsk.fusion.Occurrence = occs.item(1)
    mat: adsk.core.Matrix3D = occ.transform

    # Matrix translation, moving the sphere up by 10 units along Z axis
    mat.translation = adsk.core.Vector3D.create(0, 0, 10)

    # Set transform
    occ.transform = mat

    # Snapshot - Determining the position is important!!!
    design.snapshots.add()

    # Cut the sphere/box intersection from the box to leave a concave face
    part: adsk.fusion.BRepBody = getBodyFromBooleanOperation(design, box, sphere)
    return part

def createBox(design: adsk.fusion.Design, sizeX: float, sizeY: float, sizeZ: float) -> adsk.fusion.BRepBody:
    ''' Creates a sample box'''
    component: adsk.fusion.Component = design.rootComponent
    # Create sketch
    sketches: adsk.fusion.Sketches = component.sketches
    sketch: adsk.fusion.Sketch = sketches.add(component.xYConstructionPlane)
    lines: adsk.fusion.SketchLines = sketch.sketchCurves.sketchLines
    lines.addTwoPointRectangle(adsk.core.Point3D.create(-sizeX / 2, -sizeY / 2, 0), adsk.core.Point3D.create(sizeX / 2, sizeY / 2, 0))
    prof: adsk.fusion.Profile = sketch.profiles.item(0)
    extrudes: adsk.fusion.ExtrudeFeatures = component.features.extrudeFeatures
    distance = adsk.core.ValueInput.createByReal(sizeZ)
    ext: adsk.fusion.ExtrudeFeature = extrudes.addSimple(prof, distance, adsk.fusion.FeatureOperations.NewComponentFeatureOperation)
    return ext.bodies.item(0)

def createSphere(design: adsk.fusion.Design, radius: float) -> adsk.fusion.BRepBody:
    ''' Creates a sample sphere '''
    component: adsk.fusion.Component = design.rootComponent
    # Create a new sketch on the xy plane.
    sketches: adsk.fusion.Sketches = component.sketches
    xyPlane: adsk.fusion.ConstructionPlane = component.xYConstructionPlane
    sketch: adsk.fusion.Sketch = sketches.add(xyPlane)
    # Draw a circle.
    circles: adsk.fusion.SketchCircles = sketch.sketchCurves.sketchCircles
    circles.addByCenterRadius(adsk.core.Point3D.create(0, 0, 0), radius)
    # Draw a line to use as the axis of revolution.
    lines: adsk.fusion.SketchLines = sketch.sketchCurves.sketchLines
    axisLine: adsk.fusion.SketchLine = lines.addByTwoPoints(adsk.core.Point3D.create(-radius, 0, 0), adsk.core.Point3D.create(radius, 0, 0))
    # Get the profile defined by half of the circle.
    prof: adsk.fusion.Profile = sketch.profiles.item(0)
    # Create an revolution input for a revolution while specifying the profile and that a new component is to be created
    revolves: adsk.fusion.RevolveFeatures = component.features.revolveFeatures
    revInput: adsk.fusion.RevolveFeatureInput = revolves.createInput(prof, axisLine, adsk.fusion.FeatureOperations.NewComponentFeatureOperation)
    # Define that the extent is an angle of 2*pi to get a sphere
    angle = adsk.core.ValueInput.createByReal(2*math.pi)
    revInput.setAngleExtent(False, angle)
    # Create the extrusion.
    ext: adsk.fusion.RevolveFeature = revolves.add(revInput)
    return ext.bodies.item(0)

def getBodyFromBooleanOperation(design: adsk.fusion.Design, body1: adsk.fusion.BRepBody, body2: adsk.fusion.BRepBody) -> adsk.fusion.BRepBody:
    """ Creates a boolean operation between two bodies """
    model: adsk.fusion.Component = design.activeComponent
    features: adsk.fusion.Features = model.features
    # Create a collection and add our sphere
    bodyCollection = adsk.core.ObjectCollection.create()
    bodyCollection.add(body2)

    # Create a CombineFeatureInput using our box (body1), sphere (bodyCollection) specifying a 'cut' operation
    combineFeatures: adsk.fusion.CombineFeatures = features.combineFeatures
    combineFeatureInput: adsk.fusion.CombineFeatureInput = combineFeatures.createInput(body1, bodyCollection)
    combineFeatureInput.operation = adsk.fusion.FeatureOperations.CutFeatureOperation
    combineFeatureInput.isKeepToolBodies = False
    combineFeatureInput.isNewComponent = False

    # Generate our combined feature
    returnValue: adsk.fusion.CombineFeature = combineFeatures.add(combineFeatureInput)
    part: adsk.fusion.BRepBody = returnValue.bodies[0]
    return part
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |