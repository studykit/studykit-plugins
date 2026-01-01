# CustomFeatureParameter.isDeletable Property![](../images/TestTubeLarge.png)

Parent Object: [CustomFeatureParameter](CustomFeatureParameter.htm)

![Preview](../images/TestTubeSmall.png)This functionality is provided as a preview
of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the
[Fusion API and Scripts](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22) forum.

Because this is a preview of future functionality, there is the possibility that it will change, which will possibly
break any existing programs that use this functionality. Because of that, you should never deliver any programs that use
any preview capabilities. For a distributed program, you should wait until it has moved from preview to released state.

Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/CustomFeatureParameter.h>

## Description

Gets if this parameter can be deleted. Parameters that have dependents cannot be deleted, and model parameters typically cannot be deleted. However, there is the possibility in uncommon workflows where a model parameter no longer has any dependents, and it was not automatically deleted. In this case, this property will return true, and the deleteMe method can delete the parameter.

## Syntax

* [Python](#Python)
* [C++](#C++)

"customFeatureParameter\_var" is a variable referencing a CustomFeatureParameter object. |

"customFeatureParameter\_var" is a variable referencing a CustomFeatureParameter object. ```` ``` #include <Fusion/Features/CustomFeatureParameter.h>  // Get the value of the property. boolean propertyValue = customFeatureParameter_var->isDeletable(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version January 2021

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |