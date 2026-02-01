# MergeFacesFeatures.add Method

Parent Object: [MergeFacesFeatures](MergeFacesFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/MergeFacesFeatures.h>

## Description

Creates a new merge face feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"mergeFacesFeatures\_var" is a variable referencing a [MergeFacesFeatures](MergeFacesFeatures.htm) object.```` ``` returnValue = mergeFacesFeatures_var.add(input) ``` ```` |

"mergeFacesFeatures\_var" is a variable referencing a [MergeFacesFeatures](MergeFacesFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if successful. Because this is limited to direct modelling only that directly modifies the B-Rep body and does not create a MergeFacesFeature object there is nothing to return besides if the merge was successful or no. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| input | [MergeFacesFeatureInput](MergeFacesFeatureInput.htm) | A MergeFacesFeatureInput object that defines the desired merge. Use the createInput method to create a new MergeFacesFeatureInput object and then use methods on it (the MergeFacesFeatureInput object) to define the merge. |

## Version

Introduced in version September 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |