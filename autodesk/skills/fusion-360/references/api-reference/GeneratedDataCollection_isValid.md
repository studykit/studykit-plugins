# GeneratedDataCollection.isValid Property

Parent Object: [GeneratedDataCollection](GeneratedDataCollection.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/GeneratedData/GeneratedDataCollection.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"generatedDataCollection\_var" is a variable referencing a GeneratedDataCollection object. |

"generatedDataCollection\_var" is a variable referencing a GeneratedDataCollection object. ```` ``` #include <Cam/GeneratedData/GeneratedDataCollection.h>  // Get the value of the property. boolean propertyValue = generatedDataCollection_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version July 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |