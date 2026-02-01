# BRepBody.revisionId Property

Parent Object: [BRepBody](BRepBody.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/BRepBody.h>

## Description

Returns the current revision ID of the body. This ID changes any time the body is modified in any way. By getting and saving the ID when you create any data that is dependent on the body, you can then compare the saved ID with the current ID to determine if the body has changed to know if you should update your data.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bRepBody\_var" is a variable referencing a BRepBody object. |

"bRepBody\_var" is a variable referencing a BRepBody object. ```` ``` #include <Fusion/BRep/BRepBody.h>  // Get the value of the property. string propertyValue = bRepBody_var->revisionId(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [BRep Body Sample](BRepBodySample_Sample.htm) | B-Rep (Boundary Representation) body related functions |

## Version

Introduced in version September 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |