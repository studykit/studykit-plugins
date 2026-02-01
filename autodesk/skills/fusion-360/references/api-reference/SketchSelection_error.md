# SketchSelection.error Property

Parent Object: [SketchSelection](SketchSelection.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/GeometrySelections/SketchSelection.h>

## Description

Gets the last warning string encountered after the selection was applied to a parent.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchSelection\_var" is a variable referencing a SketchSelection object. |

"sketchSelection\_var" is a variable referencing a SketchSelection object. ```` ``` #include <Cam/GeometrySelections/SketchSelection.h>  // Get the value of the property. string propertyValue = sketchSelection_var->error(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version July 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |