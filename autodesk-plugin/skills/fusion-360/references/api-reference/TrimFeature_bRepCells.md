# TrimFeature.bRepCells Property

Parent Object: [TrimFeature](TrimFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/TrimFeature.h>

## Description

Gets the set of valid cells that have been calculated based on the current inputs. To get this collection the model must be in the state it was when the feature was initially computed, which means the timeline marker must be positioned to immediately before this feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"trimFeature\_var" is a variable referencing a TrimFeature object.  ```` ``` # Get the value of the property. propertyValue = trimFeature_var.bRepCells ``` ```` |

"trimFeature\_var" is a variable referencing a TrimFeature object. ```` ``` #include <Fusion/Features/TrimFeature.h>  // Get the value of the property. Ptr<BRepCells> propertyValue = trimFeature_var->bRepCells(); ``` ```` |

## Property Value

This is a read only property whose value is a [BRepCells](BRepCells.htm).

## Version

Introduced in version July 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |