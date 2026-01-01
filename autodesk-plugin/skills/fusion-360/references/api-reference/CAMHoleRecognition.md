# CAMHoleRecognition Object

Derived from: [OperationBase](OperationBase.htm) Object

Defined in namespace "adsk::cam" and the header file is <Cam/CAM/CAMHoleRecognition.h>

## Description

Object that represents a hole recognition object in an existing Setup, Folder or Pattern.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [activate](CAMHoleRecognition_activate.htm) | Set this object as the default container. |
| [classType](CAMHoleRecognition_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [copyAfter](CAMHoleRecognition_copyAfter.htm) | Creates a duplicate of the operation in the tree after the given operation. Throws an exception if a not allowed copy operation is made for example copying a operation out of a setup. |
| [copyBefore](CAMHoleRecognition_copyBefore.htm) | Creates a duplicate of the operation in the tree before the given operation. Throws an exception if a not allowed copy operation is made for example copying a operation out of a setup. |
| [copyInto](CAMHoleRecognition_copyInto.htm) | Creates a duplicate of the operation into the given container. You can only copy into containers, such as setups or folders. Copied operation will be copied at the end of all operations already in the container. Throws an exception if a not allowed copy operation is made for example copying a setup into a setup. |
| [deleteMe](CAMHoleRecognition_deleteMe.htm) | Deletes the operation from the document. In case of a setup or folder, all containing child operations will be deleted as well. Note: Child classes may overwrite this function and throw an exception if the object cannot be deleted. |
| [duplicate](CAMHoleRecognition_duplicate.htm) | Creates a duplicate of the operation in the tree after the itself. |
| [modifyUtility](CAMHoleRecognition_modifyUtility.htm) | Get ModifyUtility for the current operation by given utility type. |
| [moveAfter](CAMHoleRecognition_moveAfter.htm) | Move operation in tree after the given operation. Throws an exception if a not allowed move is made for example moving a operation out of a setup. |
| [moveBefore](CAMHoleRecognition_moveBefore.htm) | Move operation in tree before the given operation. Throws an exception if a not allowed move is made for example moving a operation out of a setup. |
| [moveInto](CAMHoleRecognition_moveInto.htm) | Move operation in tree into the given container. This only works with setups, patterns and folders. Moved operation will be moved at the end of all operations already in the container. Throws an exception if a not allowed move is made for example moving a setup into a setup. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [allOperations](CAMHoleRecognition_allOperations.htm) | Returns an array containing all of the operations in this hole recognition. This includes all operations nested in folders and patterns. |
| [attributes](CAMHoleRecognition_attributes.htm) | Returns the collection of attributes associated with this object. |
| [children](CAMHoleRecognition_children.htm) | Returns a collection containing all of the immediate (top level) child operations, folders and patterns in this folder in the order they appear in the browser. |
| [error](CAMHoleRecognition_error.htm) | Returns a message corresponding to any active error associated with the value of this parameter. |
| [folders](CAMHoleRecognition_folders.htm) | Returns the Folders collection that provides access to existing folders in this hole recognition. |
| [generatedDataCollection](CAMHoleRecognition_generatedDataCollection.htm) | Get the generated data associated with a given operation base instance. The type of data depends on the strategy type and might not be available for all strategy types. The available types can be found in GeneratedData.cs |
| [hasError](CAMHoleRecognition_hasError.htm) | Gets if errors were encountered when generating the operation. |
| [hasWarning](CAMHoleRecognition_hasWarning.htm) | Gets if problems were encountered when generating the operation. |
| [isActive](CAMHoleRecognition_isActive.htm) | Gets if this hole recognition is active. |
| [isLightBulbOn](CAMHoleRecognition_isLightBulbOn.htm) | Gets if this operation is currently visible in the graphics window. Use the isLightBulbOn to change if the eye icon beside the operation node in the browser is on or not. Parent nodes in the browser can have their light bulb off which affects all of their children so this property does not indicate if the operation is actually visible, just that it should be visible if all of its parent nodes are also visible. Use the isVisible property to determine if it's actually visible. |
| [isOptional](CAMHoleRecognition_isOptional.htm) | Gets and sets the "Optional" property value of the operation. Gets/sets true if the operation is optional. |
| [isProtected](CAMHoleRecognition_isProtected.htm) | Gets and sets the "protected" property value of the operation. Gets/sets true if the operation is protected. |
| [isSelected](CAMHoleRecognition_isSelected.htm) | Gets if this operation is selected in the 'Setups' browser. |
| [isSuppressed](CAMHoleRecognition_isSuppressed.htm) | Gets and sets the "Suppressed" property value of the operation. Gets/sets true if the operation is suppressed. |
| [isValid](CAMHoleRecognition_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [isVisible](CAMHoleRecognition_isVisible.htm) | Gets if this operation is currently visible in the graphics window. Use the isLightBulbOn to change if the eye icon beside the operation node in the browser is on or not. Parent nodes in the browser can have their light bulb off which affects all of their children. This property indicates the final result and whether this operation is actually visible or not. |
| [name](CAMHoleRecognition_name.htm) | Gets and sets the name of the operation as seen in the browser. This name is unique as compared to the names of all other operations in the document. |
| [notes](CAMHoleRecognition_notes.htm) | Gets and sets the notes of the operation. |
| [objectType](CAMHoleRecognition_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [operationId](CAMHoleRecognition_operationId.htm) | Returns the id of the operation. This id is unique as compared to the ids of all other operations in the document. This id will not change when changing the order or parent of the operation. This id will remain valid when the document is saved and reloaded. |
| [operations](CAMHoleRecognition_operations.htm) | Returns the Operations collection that provides access to existing individual operations in this hole recognition. |
| [parameters](CAMHoleRecognition_parameters.htm) | Gets the CAMParameters collection for this operation. |
| [parent](CAMHoleRecognition_parent.htm) | Returns the parent Setup, Folder or Pattern for this Folder. |
| [parentSetup](CAMHoleRecognition_parentSetup.htm) | Gets the Setup this operation belongs to. |
| [strategy](CAMHoleRecognition_strategy.htm) | Gets the name of the strategy associated with this operation. |
| [warning](CAMHoleRecognition_warning.htm) | Returns a message corresponding to any active warning associated with the value of this parameter. |

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |