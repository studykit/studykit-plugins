# DocumentEventArgs.cancelReason Property

Parent Object: [DocumentEventArgs](DocumentEventArgs.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/DocumentEventArgs.h>

## Description

Gets and sets the description of the reason why the operation is being canceled. This property is only used if isOperationCancelled is set to true.

## Syntax

* [Python](#Python)
* [C++](#C++)

"documentEventArgs\_var" is a variable referencing a DocumentEventArgs object. |

"documentEventArgs\_var" is a variable referencing a DocumentEventArgs object. ```` ``` #include <Core/Application/DocumentEventArgs.h>  // Get the value of the property. string propertyValue = documentEventArgs_var->cancelReason();  // Set the value of the property, where value_var is a string. bool returnValue = documentEventArgs_var->cancelReason(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Version

Introduced in version October 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |