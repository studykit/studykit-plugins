# Features.shellFeatures Property

Parent Object: [Features](Features.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/Features.h>

## Description

Returns the collection that provides access to the shell features within the component and supports the creation of new shell features.

## Syntax

* [Python](#Python)
* [C++](#C++)

"features\_var" is a variable referencing a Features object. |

"features\_var" is a variable referencing a Features object. ```` ``` #include <Fusion/Features/Features.h>  // Get the value of the property. Ptr<ShellFeatures> propertyValue = features_var->shellFeatures(); ``` ```` |

## Property Value

This is a read only property whose value is a [ShellFeatures](ShellFeatures.htm).

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