# ShellFeatures.add Method

Parent Object: [ShellFeatures](ShellFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ShellFeatures.h>

## Description

Creates a new shell feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"shellFeatures\_var" is a variable referencing a [ShellFeatures](ShellFeatures.htm) object.```` ``` returnValue = shellFeatures_var.add(input) ``` ```` |

"shellFeatures\_var" is a variable referencing a [ShellFeatures](ShellFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ShellFeature](ShellFeature.htm) | Returns the newly created ShellFeature object or null if the creation failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| input | [ShellFeatureInput](ShellFeatureInput.htm) | A ShellFeatureInput object that defines the desired shell. Use the createInput method to create a new ShellFeatureInput object and then use methods on it (the ShellFeatureInput object) to define the shell. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [shellFeatures.add](shelFeatures_add_Sample.htm) | Demonstrates creating a shell feature. |
| [Shell Feature API Sample](ShellFeatureSample_Sample.htm) | Demonstrates creating a new shell feature. |

## Version

Introduced in version November 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |