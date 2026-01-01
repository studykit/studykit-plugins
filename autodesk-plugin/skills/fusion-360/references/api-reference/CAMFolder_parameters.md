# CAMFolder.parameters Property

Parent Object: [CAMFolder](CAMFolder.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/CAM/CAMFolder.h>

## Description

Gets the CAMParameters collection for this operation.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cAMFolder\_var" is a variable referencing a CAMFolder object. |

"cAMFolder\_var" is a variable referencing a CAMFolder object. ```` ``` #include <Cam/CAM/CAMFolder.h>  // Get the value of the property. Ptr<CAMParameters> propertyValue = cAMFolder_var->parameters(); ``` ```` |

## Property Value

This is a read only property whose value is a [CAMParameters](CAMParameters.htm).

## Version

Introduced in version September 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |