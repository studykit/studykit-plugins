# NCProgram Object

Derived from: [OperationBase](OperationBase.htm) Object

Defined in namespace "adsk::cam" and the header file is <Cam/NCProgram/NCProgram.h>

## Description

Object that represents an existing NC program.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](NCProgram_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [copyAfter](NCProgram_copyAfter.htm) | Creates a duplicate of the operation in the tree after the given operation. Throws an exception if a not allowed copy operation is made for example copying a operation out of a setup. |
| [copyBefore](NCProgram_copyBefore.htm) | Creates a duplicate of the operation in the tree before the given operation. Throws an exception if a not allowed copy operation is made for example copying a operation out of a setup. |
| [copyInto](NCProgram_copyInto.htm) | Creates a duplicate of the operation into the given container. You can only copy into containers, such as setups or folders. Copied operation will be copied at the end of all operations already in the container. Throws an exception if a not allowed copy operation is made for example copying a setup into a setup. |
| [deleteMe](NCProgram_deleteMe.htm) | Deletes the operation from the document. In case of a setup or folder, all containing child operations will be deleted as well. Note: Child classes may overwrite this function and throw an exception if the object cannot be deleted. |
| [duplicate](NCProgram_duplicate.htm) | Creates a duplicate of the operation in the tree after the itself. |
| [modifyUtility](NCProgram_modifyUtility.htm) | Get ModifyUtility for the current operation by given utility type. |
| [moveAfter](NCProgram_moveAfter.htm) | Move operation in tree after the given operation. Throws an exception if a not allowed move is made for example moving a operation out of a setup. |
| [moveBefore](NCProgram_moveBefore.htm) | Move operation in tree before the given operation. Throws an exception if a not allowed move is made for example moving a operation out of a setup. |
| [moveInto](NCProgram_moveInto.htm) | Move operation in tree into the given container. This only works with setups, patterns and folders. Moved operation will be moved at the end of all operations already in the container. Throws an exception if a not allowed move is made for example moving a setup into a setup. |
| [postProcess](NCProgram_postProcess.htm) | Creates machine-specific NC code for this NC program. |
| [updatePostParameters](NCProgram_updatePostParameters.htm) | Overrides the default post parameters of this NC program with the given user's input. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [attributes](NCProgram_attributes.htm) | Returns the collection of attributes associated with this object. |
| [error](NCProgram_error.htm) | Returns a message corresponding to any active error associated with the value of this parameter. |
| [filteredOperations](NCProgram_filteredOperations.htm) | Gets all valid operations derived from the operations property. The list is ordered with respect to the nc\_program\_oderByTool parameter and considers the number of instances in a setup. |
| [fusionHubFolder](NCProgram_fusionHubFolder.htm) | Gets and sets the DataFolder to which the exported files should be uploaded to if the parameter nc\_program\_postToFusionTeam is set to true. When a DataFolder is set, nc\_program\_postToFusionTeam is automatically set to true. An exception will be thrown if the DataFolder to set is not valid or not accessible. Depending on the FusionHubExecutionBehaviors used for the export the design may be saved at this location as well. |
| [generatedDataCollection](NCProgram_generatedDataCollection.htm) | Get the generated data associated with a given operation base instance. The type of data depends on the strategy type and might not be available for all strategy types. The available types can be found in GeneratedData.cs |
| [hasError](NCProgram_hasError.htm) | Gets if errors were encountered when generating the operation. |
| [hasWarning](NCProgram_hasWarning.htm) | Gets if problems were encountered when generating the operation. |
| [isLightBulbOn](NCProgram_isLightBulbOn.htm) | Gets if this operation is currently visible in the graphics window. Use the isLightBulbOn to change if the eye icon beside the operation node in the browser is on or not. Parent nodes in the browser can have their light bulb off which affects all of their children so this property does not indicate if the operation is actually visible, just that it should be visible if all of its parent nodes are also visible. Use the isVisible property to determine if it's actually visible. |
| [isOptional](NCProgram_isOptional.htm) | Gets and sets the "Optional" property value of the operation. Gets/sets true if the operation is optional. |
| [isProtected](NCProgram_isProtected.htm) | Gets and sets the "protected" property value of the operation. Gets/sets true if the operation is protected. |
| [isSelected](NCProgram_isSelected.htm) | Gets if this operation is selected in the 'Setups' browser. |
| [isSuppressed](NCProgram_isSuppressed.htm) | Gets and sets the "Suppressed" property value of the operation. Gets/sets true if the operation is suppressed. |
| [isValid](NCProgram_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [isVisible](NCProgram_isVisible.htm) | Gets if this operation is currently visible in the graphics window. Use the isLightBulbOn to change if the eye icon beside the operation node in the browser is on or not. Parent nodes in the browser can have their light bulb off which affects all of their children. This property indicates the final result and whether this operation is actually visible or not. |
| [machine](NCProgram_machine.htm) | Gets and sets the machine of this NC program. When a machine is set, "use machine configuration" is automatically set to true. If this machine has a default post assigned, this post will be set for the NC program as well. |
| [name](NCProgram_name.htm) | Gets and sets the name of the operation as seen in the browser. This name is unique as compared to the names of all other operations in the document. |
| [notes](NCProgram_notes.htm) | Gets and sets the notes of the operation. |
| [objectType](NCProgram_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [operationId](NCProgram_operationId.htm) | Returns the id of the operation. This id is unique as compared to the ids of all other operations in the document. This id will not change when changing the order or parent of the operation. This id will remain valid when the document is saved and reloaded. |
| [operations](NCProgram_operations.htm) | Gets and sets the operations which will be included in the NC program. Valid input contains any number of operations, setups or folders. For setups and folders all child operations will be added. Operations will be post processed in setup order, with operations from the same setup grouped together. Setting the nc\_program\_orderByTool BooleanParameterValue on the parameters property to true will reorder operations across multiple setups to reduce the number of tool changes. |
| [parameters](NCProgram_parameters.htm) | Gets the CAMParameters collection for this operation. |
| [parentSetup](NCProgram_parentSetup.htm) | Gets the Setup this operation belongs to. |
| [postConfiguration](NCProgram_postConfiguration.htm) | Gets and sets the post configuration of this NC program. |
| [postParameters](NCProgram_postParameters.htm) | Gets the post parameters of this NC program. |
| [strategy](NCProgram_strategy.htm) | Gets the name of the strategy associated with this operation. |
| [warning](NCProgram_warning.htm) | Returns a message corresponding to any active warning associated with the value of this parameter. |

## Accessed From

[NCPrograms.add](NCPrograms_add.htm), [NCPrograms.item](NCPrograms_item.htm), [NCPrograms.itemByName](NCPrograms_itemByName.htm), [NCPrograms.itemByOperationId](NCPrograms_itemByOperationId.htm)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Manufacturing Workflow API Sample](ManufacturingWorkflowAPISample_Sample.htm) | Manufacturing Workflow API Sample This sample script starts by creating a simple component which is then used to describe a milling workflow. It creates a setup, a few operations, pick some tools from a Fusion sample tool library using loops and queries and ends up post-processing the operations out using an NC Program. |
| [Turning Workflow API Sample](Turning_Workflow_API_Sample_Sample.htm) | Turning Workflow API Sample This sample script starts by opening a simple component which is then used to describe a basic turning workflow. It creates a setup, a few operations, pick some tools from a Fusion sample tool library using loops and queries and ends up post-processing the operations out using an NC Program. |

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |