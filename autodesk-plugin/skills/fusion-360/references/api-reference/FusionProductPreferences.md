# FusionProductPreferences Object

Derived from: [ProductPreferences](ProductPreferences.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/FusionProductPreferences.h>

## Description

Fusion General Design Preferences

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](FusionProductPreferences_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [defaultDesignType](FusionProductPreferences_defaultDesignType.htm) | Gets and sets the default modeling type setting |
| [defaultWorkspace](FusionProductPreferences_defaultWorkspace.htm) | Gets and sets the Default workspace setting. (Model, Sculpt or Patch) |
| [is3DSketchingAllowed](FusionProductPreferences_is3DSketchingAllowed.htm) | Gets and sets the Allow 3D sketching of lines and splines option which controls if 3D sketching is allowed or if sketching is forced to be on the x-y plane of the sketch. |
| [isActiveComponentVisibilityUsed](FusionProductPreferences_isActiveComponentVisibilityUsed.htm) | Gets and sets the Active Component Visibility option |
| [isAllowReferencesDuringEditInPlace](FusionProductPreferences_isAllowReferencesDuringEditInPlace.htm) | Gets and sets if you can create associative references while editing external components in context. |
| [isAutoHideSketchOnFeatureCreation](FusionProductPreferences_isAutoHideSketchOnFeatureCreation.htm) | Gets and sets if the sketch should be automatically hidden whenever a feature is created from it. |
| [isAutoLookAtSketch](FusionProductPreferences_isAutoLookAtSketch.htm) | \*\*RETIRED\*\* This property has been replaced by the isAutoLookAtSketch2 property, which provides the full capabilities. |
| [isAutoLookAtSketch2](FusionProductPreferences_isAutoLookAtSketch2.htm) | Gets and sets if the view is re-oriented to view the newly created sketch, and if it is re-oriented, if the camera uses the current camera settings or is orthographic. |
| [isAutoProjectEdgesOnReference](FusionProductPreferences_isAutoProjectEdgesOnReference.htm) | Gets and sets if model edges should be automatically projected when creating constraints and dimensions in the active sketch when the orientation is normal to the active sketch plane. |
| [isAutoProjectGeometry](FusionProductPreferences_isAutoProjectGeometry.htm) | Gets and Sets if geometry, not in the active sketch plane, is to be automatically projected. |
| [isDimensionEditedWhenCreated](FusionProductPreferences_isDimensionEditedWhenCreated.htm) | Gets and sets if dimension value is edited when the dimension is created. |
| [isEnableArrangeAndSimplifyTools](FusionProductPreferences_isEnableArrangeAndSimplifyTools.htm) | Gets and sets if the Arrange, Remove Features, Remove Faces, and Replace with Primitives commands should be added to the Modify menu in the Design workspace. |
| [isFirstComponentGroundToParent](FusionProductPreferences_isFirstComponentGroundToParent.htm) |  |
| [isGhostedResultBodyShown](FusionProductPreferences_isGhostedResultBodyShown.htm) | Gets and sets the Show ghosted result body option |
| [isJointPreviewAnimated](FusionProductPreferences_isJointPreviewAnimated.htm) | Gets and sets the Animate joint preview option |
| [isSketchScaledWithFirstDimension](FusionProductPreferences_isSketchScaledWithFirstDimension.htm) | Gets and sets if the sketch geometry is automatically scaled when the first dimension is added. |
| [isValid](FusionProductPreferences_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [name](FusionProductPreferences_name.htm) | Returns the name of this ProductPreferences object. |
| [objectType](FusionProductPreferences_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |