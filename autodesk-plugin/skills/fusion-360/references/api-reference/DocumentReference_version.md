# DocumentReference.version Property

Parent Object: [DocumentReference](DocumentReference.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/DocumentReference.h>

## Description

Gets and sets the version of the dataFile on A360 that this document currently represents. Setting this property will cause all occurrences referencing this document to update to that version.

## Syntax

* [Python](#Python)
* [C++](#C++)

"documentReference\_var" is a variable referencing a DocumentReference object. |

"documentReference\_var" is a variable referencing a DocumentReference object. ```` ``` #include <Core/Application/DocumentReference.h>  // Get the value of the property. integer propertyValue = documentReference_var->version();  // Set the value of the property, where value_var is an integer. bool returnValue = documentReference_var->version(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an integer.

## Version

Introduced in version June 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |