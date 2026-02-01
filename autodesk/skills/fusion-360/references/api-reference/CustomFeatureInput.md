# CustomFeatureInput Object ![Preview](../images/TestTubeLarge.png)

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/CustomFeatureInput.h>

![Preview](../images/TestTubeSmall.png)This functionality is provided as a preview
of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the
[Fusion API and Scripts](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22) forum.

Because this is a preview of future functionality, there is the possibility that it will change, which will possibly
break any existing programs that use this functionality. Because of that, you should never deliver any programs that use
any preview capabilities. For a distributed program, you should wait until it has moved from preview to released state.

## Description

This class defines the methods and properties that pertain to the definition of a Ruled Surface feature.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [addCustomParameter](CustomFeatureInput_addCustomParameter.htm) | Defines the information needed to create a new custom parameter that will be associated with this feature. A custom parameter appears as a model parameter and will be listed as a child of the custom feature in the parameter dialog. The custom feature will automatically have a dependency on this parameter. |
| [addDependency](CustomFeatureInput_addDependency.htm) | Adds an entity or parameter this feature is dependent on. This is used by Fusion to know when to recompute this feature and to control the behavior of the feature's node in the timeline. |
| [classType](CustomFeatureInput_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [setStartAndEndFeatures](CustomFeatureInput_setStartAndEndFeatures.htm) | Sets the start and end features that the custom feature will group. A "feature" in this case is an object that is visible in the timeline, such as modeling features, sketches, and construction geometry. The custom feature will group the input start and end features and all features between them in the timeline. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [features](CustomFeatureInput_features.htm) | Returns the features that are grouped by this custom feature. The start and end features and all of the features between them in the timeline are returned. This includes all entities represented in the timeline including modeling features, construction geometry, sketches, etc. |
| [isValid](CustomFeatureInput_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](CustomFeatureInput_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[CustomFeatures.createInput](CustomFeatures_createInput.htm)

## Version

Introduced in version January 2021

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |