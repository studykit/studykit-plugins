# SketchSelection.hasError Property

Parent Object: [SketchSelection](SketchSelection.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/GeometrySelections/SketchSelection.h>

## Description

Gets if errors were encountered when applying the selection to a a parent.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchSelection\_var" is a variable referencing a SketchSelection object. |

"sketchSelection\_var" is a variable referencing a SketchSelection object. ```` ``` #include <Cam/GeometrySelections/SketchSelection.h>  // Get the value of the property. boolean propertyValue = sketchSelection_var->hasError(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version July 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |