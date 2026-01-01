# ArrangeFeatures.add Method

Parent Object: [ArrangeFeatures](ArrangeFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Arrange/ArrangeFeatures.h>

## Description

Creates a new Arrange feature. Use the create2DInput or create3DInput method to first create an input object and fully define the required input. Then, pass that input object to the add method to create the Arrange feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"arrangeFeatures\_var" is a variable referencing an [ArrangeFeatures](ArrangeFeatures.htm) object.```` ``` returnValue = arrangeFeatures_var.add(input) ``` ```` |

"arrangeFeatures\_var" is a variable referencing an [ArrangeFeatures](ArrangeFeatures.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ArrangeFeature](ArrangeFeature.htm) | Returns the newly created ArrangeFeature object. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| input | [ArrangeFeatureInput](ArrangeFeatureInput.htm) | The ArrangeFeature2DInput or ArrangeFeature3DInput object that defines the required information needed to create a new Arrange feature. An ArrangeFeatureInput object is the logical equivalent to the command dialog when creating an Arrange feature. It provides access to the various options and collects all of the required input when creating an Arrange feature and call the add method is the API equivalent to clicking the OK button on the command dialog to create the Arrange feature. |

## Version

Introduced in version January 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |