# RuledSurfaceFeatures.add Method

Parent Object: [RuledSurfaceFeatures](RuledSurfaceFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/RuledSurfaceFeatures.h>

## Description

Creates a new RuledSurface feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"ruledSurfaceFeatures\_var" is a variable referencing a [RuledSurfaceFeatures](RuledSurfaceFeatures.htm) object.```` ``` returnValue = ruledSurfaceFeatures_var.add(input) ``` ```` |

"ruledSurfaceFeatures\_var" is a variable referencing a [RuledSurfaceFeatures](RuledSurfaceFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [RuledSurfaceFeature](RuledSurfaceFeature.htm) | Returns the newly created RuledSurfaceFeature object or null if the creation failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| input | [RuledSurfaceFeatureInput](RuledSurfaceFeatureInput.htm) | An RuledSurfaceFeatureInput object that defines the desired RuledSurface feature. Use the createInput method to create a new RuledSurfaceFeatureInput object and then use methods on it (the RuledSurfaceFeatureInput object) to define the desired options for the ruled surface feature. |

## Version

Introduced in version September 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |