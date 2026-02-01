# Setup Object

Derived from: [OperationBase](OperationBase.htm) Object

Defined in namespace "adsk::cam" and the header file is <Cam/CAM/Setup.h>

## Description

Object that represents an existing Setup.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [activate](Setup_activate.htm) | Sets this object as the default container. |
| [additiveContainerByType](Setup_additiveContainerByType.htm) | Returns the additive container with the specified type. |
| [classType](Setup_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [copyAfter](Setup_copyAfter.htm) | Creates a duplicate of the operation in the tree after the given operation. Throws an exception if a not allowed copy operation is made for example copying a operation out of a setup. |
| [copyBefore](Setup_copyBefore.htm) | Creates a duplicate of the operation in the tree before the given operation. Throws an exception if a not allowed copy operation is made for example copying a operation out of a setup. |
| [copyInto](Setup_copyInto.htm) | Creates a duplicate of the operation into the given container. You can only copy into containers, such as setups or folders. Copied operation will be copied at the end of all operations already in the container. Throws an exception if a not allowed copy operation is made for example copying a setup into a setup. |
| [createFromCAMTemplate](Setup_createFromCAMTemplate.htm) | \*\*RETIRED\*\* Create new operations, folders, or patterns from the specified CAMTemplate. They are added to the end of the parent setup. |
| [createFromCAMTemplate2](Setup_createFromCAMTemplate2.htm) | Create new operations, folders, or patterns from the specified CAMTemplate. They are added to the end of the parent setup. |
| [createFromTemplate](Setup_createFromTemplate.htm) | \*\*RETIRED\*\* Create and add operations, folders or patterns from the specified template file to the end of this setup. |
| [createFromTemplateXML](Setup_createFromTemplateXML.htm) | \*\*RETIRED\*\* Create and add operations, folders or patterns from the specified template content XML to the end of this setup. |
| [deleteMe](Setup_deleteMe.htm) | Deletes the operation from the document. In case of a setup or folder, all containing child operations will be deleted as well. Note: Child classes may overwrite this function and throw an exception if the object cannot be deleted. |
| [duplicate](Setup_duplicate.htm) | Creates a duplicate of the operation in the tree after the itself. |
| [modifyUtility](Setup_modifyUtility.htm) | Get ModifyUtility for the current operation by given utility type. |
| [moveAfter](Setup_moveAfter.htm) | Move operation in tree after the given operation. Throws an exception if a not allowed move is made for example moving a operation out of a setup. |
| [moveBefore](Setup_moveBefore.htm) | Move operation in tree before the given operation. Throws an exception if a not allowed move is made for example moving a operation out of a setup. |
| [moveInto](Setup_moveInto.htm) | Move operation in tree into the given container. This only works with setups, patterns and folders. Moved operation will be moved at the end of all operations already in the container. Throws an exception if a not allowed move is made for example moving a setup into a setup. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [allOperations](Setup_allOperations.htm) | Returns an ObjectCollection containing all of the operations in this setup. This includes all operations nested in folders and patterns. |
| [attributes](Setup_attributes.htm) | Returns the collection of attributes associated with this object. |
| [children](Setup_children.htm) | Returns a collection containing all of the immediate (top level) child operations, folders and patterns in this setup, in the order they appear in the browser. |
| [error](Setup_error.htm) | Returns a message corresponding to any active error associated with the value of this parameter. |
| [fixtureEnabled](Setup_fixtureEnabled.htm) | Set this value to enable the use of fixtures for this setup. To then set the fixture models themselves use the `fixtures` property. |
| [fixtures](Setup_fixtures.htm) | Gets and sets the fixtures associated with the setup, which are represented by an ObjectCollection of models, where a model can be an Occurrence, BRepBody, or MeshBody. To be able to set models as fixtures, the fixturesEnabled property has to be set first. |
| [folders](Setup_folders.htm) | Returns the Folders collection that provides access to existing folders in this setup. |
| [generatedDataCollection](Setup_generatedDataCollection.htm) | Get the generated data associated with a given operation base instance. The type of data depends on the strategy type and might not be available for all strategy types. The available types can be found in GeneratedData.cs |
| [hasError](Setup_hasError.htm) | Gets if errors were encountered when generating the operation. |
| [hasWarning](Setup_hasWarning.htm) | Gets if problems were encountered when generating the operation. |
| [isActive](Setup_isActive.htm) | Gets if this setup is active. |
| [isLightBulbOn](Setup_isLightBulbOn.htm) | Gets if this operation is currently visible in the graphics window. Use the isLightBulbOn to change if the eye icon beside the operation node in the browser is on or not. Parent nodes in the browser can have their light bulb off which affects all of their children so this property does not indicate if the operation is actually visible, just that it should be visible if all of its parent nodes are also visible. Use the isVisible property to determine if it's actually visible. |
| [isOptional](Setup_isOptional.htm) | Gets and sets the "Optional" property value of the operation. Gets/sets true if the operation is optional. |
| [isProtected](Setup_isProtected.htm) | Gets and sets the "protected" property value of the operation. Gets/sets true if the operation is protected. |
| [isSelected](Setup_isSelected.htm) | Gets if this operation is selected in the 'Setups' browser. |
| [isSuppressed](Setup_isSuppressed.htm) | Gets and sets the "Suppressed" property value of the operation. Gets/sets true if the operation is suppressed. |
| [isValid](Setup_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [isVisible](Setup_isVisible.htm) | Gets if this operation is currently visible in the graphics window. Use the isLightBulbOn to change if the eye icon beside the operation node in the browser is on or not. Parent nodes in the browser can have their light bulb off which affects all of their children. This property indicates the final result and whether this operation is actually visible or not. |
| [machine](Setup_machine.htm) | Gets and sets the Machine associated with the setup. The returned Machine is a transient copy, so the Machine needs to be set to the Setup again to apply any changes. |
| [models](Setup_models.htm) | Gets and sets the input models associated with the setup. Passing in an empty ObjectCollection will remove all current inputs. Valid collection items are Occurrence, BRepBody, or MeshBody. |
| [name](Setup_name.htm) | Gets and sets the name of the operation as seen in the browser. This name is unique as compared to the names of all other operations in the document. |
| [notes](Setup_notes.htm) | Gets and sets the notes of the operation. |
| [objectType](Setup_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [operationId](Setup_operationId.htm) | Returns the id of the operation. This id is unique as compared to the ids of all other operations in the document. This id will not change when changing the order or parent of the operation. This id will remain valid when the document is saved and reloaded. |
| [operations](Setup_operations.htm) | Returns the Operations collection that provides access to existing operations in this setup. |
| [operationType](Setup_operationType.htm) | Gets the Operation Type. It can be MillingOperation, TurningOperation, JetOperation or AdditiveOperation. |
| [parameters](Setup_parameters.htm) | Gets the CAMParameters collection for this operation. |
| [parentSetup](Setup_parentSetup.htm) | Gets the Setup this operation belongs to. |
| [patterns](Setup_patterns.htm) | Returns the Patterns collection that provides access to existing patterns in this setup. |
| [printSetting](Setup_printSetting.htm) | Gets and sets the PrintSetting associated with the setup. |
| [stockMaterial](Setup_stockMaterial.htm) | ![Preview](../images/TestTubeSmall.png)Gets/ and sets the Stock material associated with the setup. |
| [stockMode](Setup_stockMode.htm) | Gets and sets the bodies associated with the setup. Passing in an empty ObjectCollection will remove all current bodies. Valid input is MeshBody and/or BRepBody objects. |
| [stockSolids](Setup_stockSolids.htm) | Gets and sets the stock solids associated with the setup, which are represented by an ObjectCollection of models, where a model can be an Occurrence, BRepBody, or MeshBody. StockMode has to be set to `SolidStock` otherwise this will throw an error. |
| [strategy](Setup_strategy.htm) | Gets the name of the strategy associated with this operation. |
| [visibilityManager](Setup_visibilityManager.htm) | Visibility manager for this setup. |
| [warning](Setup_warning.htm) | Returns a message corresponding to any active warning associated with the value of this parameter. |
| [workCoordinateSystem](Setup_workCoordinateSystem.htm) | Gets the Work Coordinate System associated with the setup as 4x4 matrix. From Matrix3D, Orientation and Origin data can be fetched. |

## Accessed From

[CAMAdditiveContainer.parentSetup](CAMAdditiveContainer_parentSetup.htm), [CAMFolder.parentSetup](CAMFolder_parentSetup.htm), [CAMHoleRecognition.parentSetup](CAMHoleRecognition_parentSetup.htm), [CAMPattern.parentSetup](CAMPattern_parentSetup.htm), [DocumentStockMaterialLibrary.setupsByStockMaterial](DocumentStockMaterialLibrary_setupsByStockMaterial.htm), [NCProgram.parentSetup](NCProgram_parentSetup.htm), [Operation.parentSetup](Operation_parentSetup.htm), [OperationBase.parentSetup](OperationBase_parentSetup.htm), [Setup.parentSetup](Setup_parentSetup.htm), [SetupChangeEventArgs.setup](SetupChangeEventArgs_setup.htm), [SetupEventArgs.setup](SetupEventArgs_setup.htm), [Setups.add](Setups_add.htm), [Setups.item](Setups_item.htm), [Setups.itemByName](Setups_itemByName.htm), [Setups.itemByOperationId](Setups_itemByOperationId.htm)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Additive Manufacturing MJF API Sample](AdditiveMJFManufacturingSample_Sample.htm) | Demonstrates how to automate the creation of an additive MJF manufacturing setup and arrange components within the build volume of a 3D printer.  To run the sample script, have a design with one or more components open in Fusion’s DESIGN workspace. This script will switch the UI from the DESIGN workspace to the MANUFACTURE workspace, create a new Manufacturing Model, and create an Additive Arrange using that manufacturing model as an input.  The setup will select an MJF 3D printer from Fusion’s machine library and a print setting from the print setting library. All components in the Manufacturing model will be automatically arranged within the build volume of the selected MJF machine. |
| [CAM Parameter Modification API Sample](CAMParameterChange_Sample_Sample.htm) | Demonstrates changing parameters of existing toolpaths. |
| [Create Setups From Hole Recognition API Sample](CreateSetupsFromHoleRecognition_Sample.htm) | This sample script demonstrates how to create a correctly oriented setup using Hole Recognition functionality.  The Fusion Manufacturing Extension is required for Hole Recognition.  The script starts by opening a sample model from the CAM Samples folder via its URN. The model comprises a 3 way coupling containing holes in various orientations and mounted on a fixture. A reference setup is created for the model using a simple stock mode and offsets. The Hole Recognition feature of the Fusion Manufacturing Extension creates 5 hole groups containing 11 holes between them. For each unique hole group vector captured, a new setup is created and its orientation transformed to match the vector. |
| [Generate Setup Sheets API Sample](GenerateSetupSheets_Sample_Sample.htm) | Demonstrates generating the setup sheets for an existing toolpath.. |
| [Generate Toolpaths API Sample](GenerateToolpaths_Sample_Sample.htm) | Demonstrates generating the toolpaths in the active document. |
| [Hole and Pocket Recognition API Sample](HoleAndPocketRecognition_Sample.htm) | This sample script demonstrates three different methods for feature recognition: one for holes and two for pockets.  The script starts by creating a simple component which is then used to demonstrate the three methods. After the features are recognised they are coloured and milling and drilling operations are created for each feature.  RecognizedHoleGroup returns a list of BRepFaces that can be used as selections for the drilling operation. RecognizedPocket also return some BRepFaces but it needs additional processing before the output can be used for creating machining operations.  The sample script demonstrates a couple of different methods, including finding the pocket BRepFaces and creating sketches from the recognized pockets.  This script works only if the Manufacturing Extension is active. |
| [Manufacturing Workflow API Sample](ManufacturingWorkflowAPISample_Sample.htm) | Manufacturing Workflow API Sample This sample script starts by creating a simple component which is then used to describe a milling workflow. It creates a setup, a few operations, pick some tools from a Fusion sample tool library using loops and queries and ends up post-processing the operations out using an NC Program. |
| [Create CAM Operation From Template API Sample](New_Operation_Sample_Sample.htm) | Demonstrates adding a new toolpath into the document using an existing CAM template. You can view the template [here](../ExtraFiles/face.f3dhsm-template), although it will be loaded automatically. Run the sample script within any Fusion project containing at least one setup. A new facing operation will be created at the end of each setup discovered. |
| [Post Toolpaths API Sample](PostToolpaths_Sample_Sample.htm) | Demonstrates posting toolpaths in the active document. |
| [Set Vise Origin As Setup WCS Origin API Sample](SetViseOriginAsSetupWCSOrigin_Sample.htm) | This sample script demonstrates how to define our setup WCS origin relative to our vise origin from either a component, a sketch point or a joint origin.  The Work Coordinate System is a reference point set in our CAM workspace and on our machine. All machine coordinates are drawn from the WCS. This script demonstrates defining the WCS by each of 4 alternative methods:  Setup by default with no origin defined.  Setup using vise origin as WCS origin.  Setup using a sketch point as WCS origin.  Setup using a joint origin as WCS origin. |
| [Turning Workflow API Sample](Turning_Workflow_API_Sample_Sample.htm) | Turning Workflow API Sample This sample script starts by opening a simple component which is then used to describe a basic turning workflow. It creates a setup, a few operations, pick some tools from a Fusion sample tool library using loops and queries and ends up post-processing the operations out using an NC Program. |

## Version

Introduced in version January 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |