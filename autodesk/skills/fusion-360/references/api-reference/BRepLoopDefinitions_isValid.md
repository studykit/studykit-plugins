# BRepLoopDefinitions.isValid Property

Parent Object: [BRepLoopDefinitions](BRepLoopDefinitions.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/BRepLoopDefinitions.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bRepLoopDefinitions\_var" is a variable referencing a BRepLoopDefinitions object. |

"bRepLoopDefinitions\_var" is a variable referencing a BRepLoopDefinitions object. ```` ``` #include <Fusion/BRep/BRepLoopDefinitions.h>  // Get the value of the property. boolean propertyValue = bRepLoopDefinitions_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version September 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |