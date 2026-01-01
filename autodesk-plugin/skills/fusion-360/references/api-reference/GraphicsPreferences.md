# GraphicsPreferences Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::core" and the header file is <Core/Application/GraphicsPreferences.h>

## Description

The GraphicsPreferences object provides access to the various graphics related preferences.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](GraphicsPreferences_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [autoThrottleEffects](GraphicsPreferences_autoThrottleEffects.htm) | \*\*RETIRED\*\* This property is no longer supported and has been replaced by the isDynamic property which dynamically changes the effect settings to optimize graphics performance. |
| [canvasEffects](GraphicsPreferences_canvasEffects.htm) | Provides access to the settings that control the canvas effects. |
| [degradedSelectionDisplayStyle](GraphicsPreferences_degradedSelectionDisplayStyle.htm) | Gets and sets the style of display for degraded selections. Setting this property is only valid when the graphics preset is set to "custom" and will fail if it is set to "quality" or "performance". The graphics preset can be determined by using the graphicsPreset property, as shown below. |
| [graphicsPreset](GraphicsPreferences_graphicsPreset.htm) | Gets and sets if the different graphics settings are using predefined settings to get the best performance, quality, or are custom to allow any settings. Setting this to performance or quality will result in other graphics settings changing to match the defined preset. |
| [hiddenEdgeDimming](GraphicsPreferences_hiddenEdgeDimming.htm) | Gets and sets the dimming percentage to use for hidden edges. the value is a percentage expressed by a value between 0 and 100. Setting this property is only valid when the graphics preset is set to "custom" and will fail if it is set to "quality" or "performance". The graphics preset can be determined by using the graphicsPreset property, as shown below.   Application.preferences.graphicsPreferences.graphicsPreset |
| [isAnimateViewTransitions](GraphicsPreferences_isAnimateViewTransitions.htm) | Gets and sets if the camera should be animated as it transitions from one view to another. If true, there will be an animated transition. Setting this property is only valid when the graphics preset is set to "custom" and will fail if it is set to "quality" or "performance". The graphics preset can be determined by using the graphicsPreset property, as shown below.   Application.preferences.graphicsPreferences.graphicsPreset |
| [isDynamic](GraphicsPreferences_isDynamic.htm) | Gets and sets if the value defined by minimumFramesPerSecond will be considered when processing graphics. This is the equivalent of the "Dynamic" check box in Preferences dialog. Setting this property is only valid when the graphics preset is set to "custom" and will fail if it is set to "quality" or "performance". The graphics preset can be determined by using the graphicsPreset property, as shown below.   Application.preferences.graphicsPreferences.graphicsPreset |
| [isHighResolutionCanvasGraphicsEnabled](GraphicsPreferences_isHighResolutionCanvasGraphicsEnabled.htm) | Gets and sets if high resolution canvas graphics is enabled. A value of true indicates it is enabled. Setting this property is only valid when the graphics preset is set to "custom" and will fail if it is set to "quality" or "performance". The graphics preset can be determined by using the graphicsPreset property, as shown below.   Application.preferences.graphicsPreferences.graphicsPreset |
| [isLimitEffectsDuringNavigation](GraphicsPreferences_isLimitEffectsDuringNavigation.htm) | \*\*RETIRED\*\* This property is no longer supported and has been replaced by the isDynamic property which dynamically changes the effect settings to optimize graphics performance. |
| [isSurfaceNormalDisplayDisabled](GraphicsPreferences_isSurfaceNormalDisplayDisabled.htm) | Gets and sets whether the surface normal display is disabled. Setting this property is only valid when the graphics preset is set to "custom" and will fail if it is set to "quality" or "performance". The graphics preset can be determined by using the graphicsPreset property, as shown below.   Application.preferences.graphicsPreferences.graphicsPreset |
| [isValid](GraphicsPreferences_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [isWoodBumpEnabled](GraphicsPreferences_isWoodBumpEnabled.htm) | Gets and sets whether the bump effect is enabled when supported by the Wood (Solid) and the graphics driver. Setting this property is only valid when the graphics preset is set to "custom" and will fail if it is set to "quality" or "performance". The graphics preset can be determined by using the graphicsPreset property, as shown below.   Application.preferences.graphicsPreferences.graphicsPreset |
| [minimumFramesPerSecond](GraphicsPreferences_minimumFramesPerSecond.htm) | Gets and sets the minimum frames per second. The isDynamic property must be true for this to be considered. Setting this property is only valid when the graphics preset is set to "custom" and will fail if it is set to "quality" or "performance". The graphics preset can be determined by using the graphicsPreset property, as shown below.   Application.preferences.graphicsPreferences.graphicsPreset |
| [objectType](GraphicsPreferences_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.   It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType(): |
| [selectionDisplayStyle](GraphicsPreferences_selectionDisplayStyle.htm) | Gets and sets the style of display to use for selections. Setting this property is only valid when the graphics preset is set to "custom" and will fail if it is set to "quality" or "performance". The graphics preset can be determined by using the graphicsPreset property, as shown below.   Application.preferences.graphicsPreferences.graphicsPreset |
| [transparencyEffects](GraphicsPreferences_transparencyEffects.htm) | Gets and sets the style of display for transparency effects. Setting this property is only valid when the graphics preset is set to "custom" and will fail if it is set to "quality" or "performance". The graphics preset can be determined by using the graphicsPreset property, as shown below.   Application.preferences.graphicsPreferences.graphicsPreset |

## Accessed From

[Preferences.graphicsPreferences](Preferences_graphicsPreferences.htm)

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |