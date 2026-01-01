# TrimFeatures.createInput Method

Parent Object: [TrimFeatures](TrimFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/TrimFeatures.h>

## Description

Creates a TrimFeatureInput object. Use properties and methods on this object to define the trim feature you want to create and then use the Add method, passing in the TrimFeatureInput object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"trimFeatures\_var" is a variable referencing a [TrimFeatures](TrimFeatures.htm) object.```` ``` returnValue = trimFeatures_var.createInput(trimTool) ``` ```` |

"trimFeatures\_var" is a variable referencing a [TrimFeatures](TrimFeatures.htm) object.  ```` ``` #include <Fusion/Features/TrimFeatures.h>  returnValue = trimFeatures_var->createInput(trimTool); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [TrimFeatureInput](TrimFeatureInput.htm) | Returns the newly created TrimFeatureInput object or null if the creation failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| trimTool | [Base](Base.htm) | A patch body, B-Rep face, construction plane or sketch curve that intersects the surface or surfaces to be trimmed |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [trimFeatures.add](trimFeatures_add_Sample.htm) | Demonstrates the trimFeatures.add method. |
| [Trim Feature API Sample](TrimFeatureSample_Sample.htm) | Demonstrates creating a new trim feature. |

## Version

Introduced in version July 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |