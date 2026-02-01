# TrimFeatureInput.bRepCells Property

Parent Object: [TrimFeatureInput](TrimFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/TrimFeatureInput.h>

## Description

Returns the collection of the valid cells that have been calculated based on the trim tool. Use this collection to specify which cells to trim away.

## Syntax

* [Python](#Python)
* [C++](#C++)

"trimFeatureInput\_var" is a variable referencing a TrimFeatureInput object. |

"trimFeatureInput\_var" is a variable referencing a TrimFeatureInput object. ```` ``` #include <Fusion/Features/TrimFeatureInput.h>  // Get the value of the property. Ptr<BRepCells> propertyValue = trimFeatureInput_var->bRepCells(); ``` ```` |

## Property Value

This is a read only property whose value is a [BRepCells](BRepCells.htm).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Trim Feature API Sample](TrimFeatureSample_Sample.htm) | Demonstrates creating a new trim feature. |

## Version

Introduced in version July 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |