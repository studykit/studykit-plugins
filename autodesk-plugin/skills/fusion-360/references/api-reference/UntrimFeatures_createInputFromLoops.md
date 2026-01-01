# UntrimFeatures.createInputFromLoops Method

Parent Object: [UntrimFeatures](UntrimFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/UntrimFeatures.h>

## Description

Creates an UntrimFeatureInput object that defines the input needed to create an untrim feature. Use the input object to define the input to create the desired feature and then use the Add method, passing in the UntrimFeatureInput object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"untrimFeatures\_var" is a variable referencing a [UntrimFeatures](UntrimFeatures.htm) object.```` ``` # Uses no optional arguments. ``` ```` |

"untrimFeatures\_var" is a variable referencing a [UntrimFeatures](UntrimFeatures.htm) object.  ```` ``` #include <Fusion/Features/UntrimFeatures.h>  // Uses no optional arguments. returnValue = untrimFeatures_var->createInputFromLoops(loops);  // Uses optional arguments. returnValue = untrimFeatures_var->createInputFromLoops(loops, extensionDistance); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [UntrimFeatureInput](UntrimFeatureInput.htm) | Returns the newly created UntrimFeatureInput object or null if the creation failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| loops | BRepLoop[] | Input the entities that define loops to remove. Only loops that do not have a connected face can be removed (the edges in the loop have a single face) The array can only contain loops from surface bodies, (the isSolid property of the BRepBody returns false). |
| extensionDistance | [ValueInput](ValueInput.htm) | If an external boundary is removed the untrimmed face can be extended by a specified distance.   This is an optional argument whose default value is null. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Untrim Feature API Sample](UntrimFeatureSample_Sample.htm) | Demonstrates creating a new untrim feature. |

## Version

Introduced in version January 2021

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |