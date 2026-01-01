# MirrorFeatures.add Method

Parent Object: [MirrorFeatures](MirrorFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/MirrorFeatures.h>

## Description

Creates a new mirror feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"mirrorFeatures\_var" is a variable referencing a [MirrorFeatures](MirrorFeatures.htm) object.```` ``` returnValue = mirrorFeatures_var.add(input) ``` ```` |

"mirrorFeatures\_var" is a variable referencing a [MirrorFeatures](MirrorFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [MirrorFeature](MirrorFeature.htm) | Returns the newly created MirrorFeature object or null if the creation failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| input | [MirrorFeatureInput](MirrorFeatureInput.htm) | A MirrorFeatureInput object that defines the desired mirror. Use the createInput method to create a new MirrorFeatureInput object and then use methods on it (the MirrorFeatureInput object) to define the mirror. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [mirrorFeatures.add](mirrorFeatures_add_Sample.htm) | Demonstrates the mirrorFeatures.add method by mirroring the selected body around the base X-Y construction plane. |

## Version

Introduced in version November 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |