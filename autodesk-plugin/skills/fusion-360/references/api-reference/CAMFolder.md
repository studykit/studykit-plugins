# CAMFolder Object

Derived from: [OperationBase](OperationBase.htm) Object

Defined in namespace "adsk::cam" and the header file is <Cam/CAM/CAMFolder.h>

## Description

Object that represents a folder in an existing Setup, Folder or Pattern.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [activate](CAMFolder_activate.htm) | Sets this object as the default container. |
| [classType](CAMFolder_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [copyAfter](CAMFolder_copyAfter.htm) | Creates a duplicate of the operation in the tree after the given operation. Throws an exception if a not allowed copy operation is made for example copying a operation out of a setup. |
| [copyBefore](CAMFolder_copyBefore.htm) | Creates a duplicate of the operation in the tree before the given operation. Throws an exception if a not allowed copy operation is made for example copying a operation out of a setup. |
| [copyInto](CAMFolder_copyInto.htm) | Creates a duplicate of the operation into the given container. You can only copy into containers, such as setups or folders. Copied operation will be copied at the end of all operations already in the container. Throws an exception if a not allowed copy operation is made for example copying a setup into a setup. |
| [createFromCAMTemplate](CAMFolder_createFromCAMTemplate.htm) | \*\*RETIRED\*\* Creates and adds operations, folders or patterns from the specified CAMTemplate to the end of this folder. |
| [createFromCAMTemplate2](CAMFolder_createFromCAMTemplate2.htm) | Create new operations, folders, or patterns from the specified CAMTemplate. They are added to the end of the parent setup. |
| [createFromTemplate](CAMFolder_createFromTemplate.htm) | \*\*RETIRED\*\* Creates and adds operations, folders or patterns from the specified template file to the end of this folder. |
| [createFromTemplateXML](CAMFolder_createFromTemplateXML.htm) | \*\*RETIRED\*\* Creates and adds operations, folders or patterns from the specified template content XML to the end of this folder. |
| [deleteMe](CAMFolder_deleteMe.htm) | Deletes the operation from the document. In case of a setup or folder, all containing child operations will be deleted as well. Note: Child classes may overwrite this function and throw an exception if the object cannot be deleted. |
| [duplicate](CAMFolder_duplicate.htm) | Creates a duplicate of the operation in the tree after the itself. |
| [modifyUtility](CAMFolder_modifyUtility.htm) | Get ModifyUtility for the current operation by given utility type. |
| [moveAfter](CAMFolder_moveAfter.htm) | Move operation in tree after the given operation. Throws an exception if a not allowed move is made for example moving a operation out of a setup. |
| [moveBefore](CAMFolder_moveBefore.htm) | Move operation in tree before the given operation. Throws an exception if a not allowed move is made for example moving a operation out of a setup. |
| [moveInto](CAMFolder_moveInto.htm) | Move operation in tree into the given container. This only works with setups, patterns and folders. Moved operation will be moved at the end of all operations already in the container. Throws an exception if a not allowed move is made for example moving a setup into a setup. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [allOperations](CAMFolder_allOperations.htm) | Gets a collection containing all of the operations in this folder. This includes all operations nested in folders and patterns. |
| [attributes](CAMFolder_attributes.htm) | Returns the collection of attributes associated with this object. |
| [children](CAMFolder_children.htm) | Returns a collection containing all of the immediate (top level) child operations, folders and patterns in this folder in the order they appear in the browser. |
| [error](CAMFolder_error.htm) | Returns a message corresponding to any active error associated with the value of this parameter. |
| [folders](CAMFolder_folders.htm) | Returns the Folders collection that provides access to existing folders in this folder. |
| [generatedDataCollection](CAMFolder_generatedDataCollection.htm) | Get the generated data associated with a given operation base instance. The type of data depends on the strategy type and might not be available for all strategy types. The available types can be found in GeneratedData.cs |
| [hasError](CAMFolder_hasError.htm) | Gets if errors were encountered when generating the operation. |
| [hasWarning](CAMFolder_hasWarning.htm) | Gets if problems were encountered when generating the operation. |
| [isActive](CAMFolder_isActive.htm) | Gets if this folder is active. |
| [isLightBulbOn](CAMFolder_isLightBulbOn.htm) | Gets if this operation is currently visible in the graphics window. Use the isLightBulbOn to change if the eye icon beside the operation node in the browser is on or not. Parent nodes in the browser can have their light bulb off which affects all of their children so this property does not indicate if the operation is actually visible, just that it should be visible if all of its parent nodes are also visible. Use the isVisible property to determine if it's actually visible. |
| [isOptional](CAMFolder_isOptional.htm) | Gets and sets the "Optional" property value of the operation. Gets/sets true if the operation is optional. |
| [isProtected](CAMFolder_isProtected.htm) | Gets and sets the "protected" property value of the operation. Gets/sets true if the operation is protected. |
| [isSelected](CAMFolder_isSelected.htm) | Gets if this operation is selected in the 'Setups' browser. |
| [isSuppressed](CAMFolder_isSuppressed.htm) | Gets and sets the "Suppressed" property value of the operation. Gets/sets true if the operation is suppressed. |
| [isValid](CAMFolder_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [isVisible](CAMFolder_isVisible.htm) | Gets if this operation is currently visible in the graphics window. Use the isLightBulbOn to change if the eye icon beside the operation node in the browser is on or not. Parent nodes in the browser can have their light bulb off which affects all of their children. This property indicates the final result and whether this operation is actually visible or not. |
| [name](CAMFolder_name.htm) | Gets and sets the name of the operation as seen in the browser. This name is unique as compared to the names of all other operations in the document. |
| [notes](CAMFolder_notes.htm) | Gets and sets the notes of the operation. |
| [objectType](CAMFolder_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [operationId](CAMFolder_operationId.htm) | Returns the id of the operation. This id is unique as compared to the ids of all other operations in the document. This id will not change when changing the order or parent of the operation. This id will remain valid when the document is saved and reloaded. |
| [operations](CAMFolder_operations.htm) | Returns the Operations collection that provides access to existing individual operations in this folder. |
| [parameters](CAMFolder_parameters.htm) | Gets the CAMParameters collection for this operation. |
| [parent](CAMFolder_parent.htm) | Returns the parent Setup, Folder or Pattern for this Folder. |
| [parentSetup](CAMFolder_parentSetup.htm) | Gets the Setup this operation belongs to. |
| [patterns](CAMFolder_patterns.htm) | Returns the Patterns collection that provides access to existing patterns in this folder. |
| [strategy](CAMFolder_strategy.htm) | Gets the name of the strategy associated with this operation. |
| [warning](CAMFolder_warning.htm) | Returns a message corresponding to any active warning associated with the value of this parameter. |

## Accessed From

[CAMFolders.addFolder](CAMFolders_addFolder.htm), [CAMFolders.item](CAMFolders_item.htm), [CAMFolders.itemByName](CAMFolders_itemByName.htm), [CAMFolders.itemByOperationId](CAMFolders_itemByOperationId.htm)

## Derived Classes

[CAMPattern](CAMPattern.htm)

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