# LoftFeatureInput.loftSections Property

Parent Object: [LoftFeatureInput](LoftFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/LoftFeatureInput.h>

## Description

The set of sections, (or profiles as they're referred to in the user-interface), that the loft will pass through. Use the add method on the LoftSections object to specify new sections.

## Syntax

* [Python](#Python)
* [C++](#C++)

"loftFeatureInput\_var" is a variable referencing a LoftFeatureInput object. |

"loftFeatureInput\_var" is a variable referencing a LoftFeatureInput object. ```` ``` #include <Fusion/Features/LoftFeatureInput.h>  // Get the value of the property. Ptr<LoftSections> propertyValue = loftFeatureInput_var->loftSections(); ``` ```` |

## Property Value

This is a read only property whose value is a [LoftSections](LoftSections.htm).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [loftFeatures.add](loftFeatures_add_Sample.htm) | Demonstrates the loftFeatures.add method. |
| [Loft Feature API Sample](LoftFeatureSample_Sample.htm) | Demonstrates creating a new loft feature. |

## Version

Introduced in version August 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |