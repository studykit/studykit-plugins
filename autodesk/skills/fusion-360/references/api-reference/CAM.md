# CAM Object

Derived from: [Product](Product.htm) Object

Defined in namespace "adsk::cam" and the header file is <Cam/CAM/CAM.h>

## Description

Object that represents the CAM environment of a Fusion document.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [checkAllToolpaths](CAM_checkAllToolpaths.htm) | Checks if all the operations (includes those nested in sub-folders or patterns) in the document are valid and up to date. |
| [checkToolpath](CAM_checkToolpath.htm) | Checks if the operations (including those nested in sub-folders or patterns) are valid and up to date. |
| [checkValidity](CAM_checkValidity.htm) | Checks whether the models used by the operations have changed in the mean time and invalidates the affected operations if needed. Should be used for cases where the automatic detection does not work yet, for instance when design changes are expected before a Manufacture API call. Also recommended at the beginning of a script or the beginning of an event handler. |
| [classType](CAM_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [clearAllToolpaths](CAM_clearAllToolpaths.htm) | Clears all the toolpaths in the document, including those nested in sub-folders or patterns. |
| [clearToolpath](CAM_clearToolpath.htm) | Clears all the toolpaths for the specified objects, including those nested in sub-folders or patterns. |
| [deleteEntities](CAM_deleteEntities.htm) | Deletes the specified set of entities that are associated with this product. |
| [export3MFForDefaultAdditiveSetup](CAM_export3MFForDefaultAdditiveSetup.htm) | \*\*RETIRED\*\* This method is only valid for an additive setup and exports the default additive setup's models as a 3MF file. The 3MF also contains machine and support information. |
| [findAttributes](CAM_findAttributes.htm) | Find attributes attached to objects in this product that match the group and or attribute name. This does not find attributes attached directly to the Product or Document objects but finds the attributes attached to entities within the product. |
| [generateAllSetupSheets](CAM_generateAllSetupSheets.htm) | Generates all of the setup sheets for all of the operations in the document |
| [generateAllToolpaths](CAM_generateAllToolpaths.htm) | Generates or regenerates all the operations in the document, including those nested in sub-folders or patterns. |
| [generateSetupSheet](CAM_generateSetupSheet.htm) | Generate the setup sheets for the specified objects |
| [generateTemplateXML](CAM_generateTemplateXML.htm) | Generates a template for the specified Operations, Setups, or Folders and returns the template as an XML string. |
| [generateToolpath](CAM_generateToolpath.htm) | Generates or regenerates all the specified objects, including those nested in sub-folders or patterns. |
| [getMachiningTime](CAM_getMachiningTime.htm) | Get the machining time for the specified objects. |
| [postProcess](CAM_postProcess.htm) | \*\*RETIRED\*\* Post all of the toolpaths (including those nested in sub-folders or patterns) for the specified objects. If post processing fails, an error message can be retrieved from the error log explaining the reason for the failure. |
| [postProcessAll](CAM_postProcessAll.htm) | \*\*RETIRED\*\* Post all of the toolpaths (includes those nested in sub-folders or patterns) in the document. If post processing fails, an error message can be retrieved from the error log explaining the reason for the failure. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [allMachines](CAM_allMachines.htm) | Gets an array containing all the machines in the document. |
| [allOperations](CAM_allOperations.htm) | Gets a collection containing all of the operations in the document. This includes all operations nested in folders and patterns. |
| [attributes](CAM_attributes.htm) | Returns the collection of attributes associated with this product. |
| [customGraphicsGroups](CAM_customGraphicsGroups.htm) | Returns the customGraphicsGroups object associated with the CAM product. |
| [designRootOccurrence](CAM_designRootOccurrence.htm) | The CAM product has its own root component which has a single occurrence that references the Design root occurrence. This property returns this occurrence. |
| [documentStockMaterialLibrary](CAM_documentStockMaterialLibrary.htm) | ![Preview](../images/TestTubeSmall.png)Gets the document StockMaterialLibrary. The StockMaterialLibrary contains all stock materials used by any setup inside the document. Changes to the original StockMaterialLibrary will not affect any setup because the document StockMaterialLibrary is an independent copy. You can only get a valid DocumentStockMaterialLibrary when you have access to Stock Materials private preview feature and enable the feature flag. |
| [documentToolLibrary](CAM_documentToolLibrary.htm) | Gets the document ToolLibrary. The ToolLibrary contains all tools used by any operation inside the document. Changes to the original ToolLibrary will not affect any operation because the document ToolLibrary is an independent copy. |
| [exportManager](CAM_exportManager.htm) | Returns the Export Manager which provides access to the functionality to export in various formats. |
| [genericPostFolder](CAM_genericPostFolder.htm) | Gets the installed post folder. |
| [isValid](CAM_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [manufacturingModels](CAM_manufacturingModels.htm) | Returns the collection of manufacturing models in the document. |
| [namedViews](CAM_namedViews.htm) | Returns the NamedViews object associated with this product. The NamedViews collection provides access to the named views defined in this product and supports the creation of new named views. |
| [ncPrograms](CAM_ncPrograms.htm) | Returns the collection of NC programs in the document. |
| [objectType](CAM_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.   It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType(): |
| [parentDocument](CAM_parentDocument.htm) | Returns the parent Document object. |
| [personalPostFolder](CAM_personalPostFolder.htm) | Gets the personal post folder. |
| [productType](CAM_productType.htm) | Returns the product type name of this product. A list of all of the possible product types can be obtained by using the Application.supportedProductTypes property. |
| [selectionSets](CAM_selectionSets.htm) | Returns the SelectionSets object associated with this product. If the product does not support selection sets, null is returned. The SelectionSets object is used to create and access existing selection sets. |
| [setups](CAM_setups.htm) | Returns the Setups collection that provides access to existing setups. |
| [temporaryFolder](CAM_temporaryFolder.htm) | Gets the folder for temporary files. |
| [unitsManager](CAM_unitsManager.htm) | Returns the UnitsManager object associated with this product. |
| [workspaces](CAM_workspaces.htm) | Returns the workspaces associated with this product. |

## Events

|  |  |
| --- | --- |
| Name | Description |
| [setupActivated](CAM_setupActivated.htm) | The SetupActivated event fires when a setup is activated. |
| [setupActivating](CAM_setupActivating.htm) | The SetupActivating event fires before a setup is activated. |
| [setupChanged](CAM_setupChanged.htm) | The SetupChanged event fires when a setup is modified. |
| [setupCreated](CAM_setupCreated.htm) | The SetupCreated event fires when a new setup is created. |
| [setupDeactivated](CAM_setupDeactivated.htm) | The SetupDeactivated event fires when a setup is deactivated. |
| [setupDeactivating](CAM_setupDeactivating.htm) | The SetupDeactivating event fires before a setup is deactivated. |
| [setupDestroying](CAM_setupDestroying.htm) | The setupDestroying event fires before a setup is destroyed. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Generate Setup Sheets API Sample](GenerateSetupSheets_Sample_Sample.htm) | Demonstrates generating the setup sheets for an existing toolpath.. |
| [Generate Toolpaths API Sample](GenerateToolpaths_Sample_Sample.htm) | Demonstrates generating the toolpaths in the active document. |
| [Manufacturing Workflow API Sample](ManufacturingWorkflowAPISample_Sample.htm) | Manufacturing Workflow API Sample This sample script starts by creating a simple component which is then used to describe a milling workflow. It creates a setup, a few operations, pick some tools from a Fusion sample tool library using loops and queries and ends up post-processing the operations out using an NC Program. |
| [Create CAM Operation From Template API Sample](New_Operation_Sample_Sample.htm) | Demonstrates adding a new toolpath into the document using an existing CAM template. You can view the template [here](../ExtraFiles/face.f3dhsm-template), although it will be loaded automatically. Run the sample script within any Fusion project containing at least one setup. A new facing operation will be created at the end of each setup discovered. |
| [Post Toolpaths API Sample](PostToolpaths_Sample_Sample.htm) | Demonstrates posting toolpaths in the active document. |
| [Turning Workflow API Sample](Turning_Workflow_API_Sample_Sample.htm) | Turning Workflow API Sample This sample script starts by opening a simple component which is then used to describe a basic turning workflow. It creates a setup, a few operations, pick some tools from a Fusion sample tool library using loops and queries and ends up post-processing the operations out using an NC Program. |

## Version

Introduced in version January 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |