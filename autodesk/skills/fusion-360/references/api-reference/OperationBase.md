# OperationBase Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::cam" and the header file is <Cam/Operations/OperationBase.h>

## Description

Base class object representing all operations, folders, patterns and setups.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](OperationBase_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [copyAfter](OperationBase_copyAfter.htm) | Creates a duplicate of the operation in the tree after the given operation. Throws an exception if a not allowed copy operation is made for example copying a operation out of a setup. |
| [copyBefore](OperationBase_copyBefore.htm) | Creates a duplicate of the operation in the tree before the given operation. Throws an exception if a not allowed copy operation is made for example copying a operation out of a setup. |
| [copyInto](OperationBase_copyInto.htm) | Creates a duplicate of the operation into the given container. You can only copy into containers, such as setups or folders. Copied operation will be copied at the end of all operations already in the container. Throws an exception if a not allowed copy operation is made for example copying a setup into a setup. |
| [deleteMe](OperationBase_deleteMe.htm) | Deletes the operation from the document. In case of a setup or folder, all containing child operations will be deleted as well. Note: Child classes may overwrite this function and throw an exception if the object cannot be deleted. |
| [duplicate](OperationBase_duplicate.htm) | Creates a duplicate of the operation in the tree after the itself. |
| [modifyUtility](OperationBase_modifyUtility.htm) | Get ModifyUtility for the current operation by given utility type. |
| [moveAfter](OperationBase_moveAfter.htm) | Move operation in tree after the given operation. Throws an exception if a not allowed move is made for example moving a operation out of a setup. |
| [moveBefore](OperationBase_moveBefore.htm) | Move operation in tree before the given operation. Throws an exception if a not allowed move is made for example moving a operation out of a setup. |
| [moveInto](OperationBase_moveInto.htm) | Move operation in tree into the given container. This only works with setups, patterns and folders. Moved operation will be moved at the end of all operations already in the container. Throws an exception if a not allowed move is made for example moving a setup into a setup. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [attributes](OperationBase_attributes.htm) | Returns the collection of attributes associated with this object. |
| [error](OperationBase_error.htm) | Returns a message corresponding to any active error associated with the value of this parameter. |
| [generatedDataCollection](OperationBase_generatedDataCollection.htm) | Get the generated data associated with a given operation base instance. The type of data depends on the strategy type and might not be available for all strategy types. The available types can be found in GeneratedData.cs |
| [hasError](OperationBase_hasError.htm) | Gets if errors were encountered when generating the operation. |
| [hasWarning](OperationBase_hasWarning.htm) | Gets if problems were encountered when generating the operation. |
| [isLightBulbOn](OperationBase_isLightBulbOn.htm) | Gets if this operation is currently visible in the graphics window. Use the isLightBulbOn to change if the eye icon beside the operation node in the browser is on or not. Parent nodes in the browser can have their light bulb off which affects all of their children so this property does not indicate if the operation is actually visible, just that it should be visible if all of its parent nodes are also visible. Use the isVisible property to determine if it's actually visible. |
| [isOptional](OperationBase_isOptional.htm) | Gets and sets the "Optional" property value of the operation. Gets/sets true if the operation is optional. |
| [isProtected](OperationBase_isProtected.htm) | Gets and sets the "protected" property value of the operation. Gets/sets true if the operation is protected. |
| [isSelected](OperationBase_isSelected.htm) | Gets if this operation is selected in the 'Setups' browser. |
| [isSuppressed](OperationBase_isSuppressed.htm) | Gets and sets the "Suppressed" property value of the operation. Gets/sets true if the operation is suppressed. |
| [isValid](OperationBase_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [isVisible](OperationBase_isVisible.htm) | Gets if this operation is currently visible in the graphics window. Use the isLightBulbOn to change if the eye icon beside the operation node in the browser is on or not. Parent nodes in the browser can have their light bulb off which affects all of their children. This property indicates the final result and whether this operation is actually visible or not. |
| [name](OperationBase_name.htm) | Gets and sets the name of the operation as seen in the browser. This name is unique as compared to the names of all other operations in the document. |
| [notes](OperationBase_notes.htm) | Gets and sets the notes of the operation. |
| [objectType](OperationBase_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [operationId](OperationBase_operationId.htm) | Returns the id of the operation. This id is unique as compared to the ids of all other operations in the document. This id will not change when changing the order or parent of the operation. This id will remain valid when the document is saved and reloaded. |
| [parameters](OperationBase_parameters.htm) | Gets the CAMParameters collection for this operation. |
| [parentSetup](OperationBase_parentSetup.htm) | Gets the Setup this operation belongs to. |
| [strategy](OperationBase_strategy.htm) | Gets the name of the strategy associated with this operation. |
| [warning](OperationBase_warning.htm) | Returns a message corresponding to any active warning associated with the value of this parameter. |

## Accessed From

[CAMFolder.createFromCAMTemplate](CAMFolder_createFromCAMTemplate.htm), [CAMFolder.createFromCAMTemplate2](CAMFolder_createFromCAMTemplate2.htm), [CAMFolder.createFromTemplateXML](CAMFolder_createFromTemplateXML.htm), [CAMHoleRecognition.allOperations](CAMHoleRecognition_allOperations.htm), [CAMPattern.createFromCAMTemplate](CAMPattern_createFromCAMTemplate.htm), [CAMPattern.createFromCAMTemplate2](CAMPattern_createFromCAMTemplate2.htm), [CAMPattern.createFromTemplateXML](CAMPattern_createFromTemplateXML.htm), [NCProgram.filteredOperations](NCProgram_filteredOperations.htm), [NCProgram.operations](NCProgram_operations.htm), [NCProgramInput.operations](NCProgramInput_operations.htm), [Operations.add](Operations_add.htm), [Setup.createFromCAMTemplate](Setup_createFromCAMTemplate.htm), [Setup.createFromCAMTemplate2](Setup_createFromCAMTemplate2.htm), [Setup.createFromTemplateXML](Setup_createFromTemplateXML.htm)

## Derived Classes

[CAMAdditiveContainer](CAMAdditiveContainer.htm), [CAMFolder](CAMFolder.htm), [CAMHoleRecognition](CAMHoleRecognition.htm), [NCProgram](NCProgram.htm), [Operation](Operation.htm), [Setup](Setup.htm)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Manufacturing Workflow API Sample](ManufacturingWorkflowAPISample_Sample.htm) | Manufacturing Workflow API Sample This sample script starts by creating a simple component which is then used to describe a milling workflow. It creates a setup, a few operations, pick some tools from a Fusion sample tool library using loops and queries and ends up post-processing the operations out using an NC Program. |

## Version

Introduced in version January 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |