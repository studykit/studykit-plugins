# DocumentEventArgs.isOperationCancelled Property

Parent Object: [DocumentEventArgs](DocumentEventArgs.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/DocumentEventArgs.h>

## Description

Gets and sets if the operation for this event is to be canceled. The description of the reason for canceling the operation can be set with the cancelReason property. This is only supported for the documentSaving event.

## Syntax

* [Python](#Python)
* [C++](#C++)

"documentEventArgs\_var" is a variable referencing a DocumentEventArgs object. |

"documentEventArgs\_var" is a variable referencing a DocumentEventArgs object. ```` ``` #include <Core/Application/DocumentEventArgs.h>  // Get the value of the property. boolean propertyValue = documentEventArgs_var->isOperationCancelled();  // Set the value of the property, where value_var is a boolean. bool returnValue = documentEventArgs_var->isOperationCancelled(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version October 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |