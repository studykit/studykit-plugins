# CustomFeature Object ![Preview](../images/TestTubeLarge.png)

Derived from: [Feature](Feature.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/CustomFeature.h>

![Preview](../images/TestTubeSmall.png)This functionality is provided as a preview
of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the
[Fusion API and Scripts](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22) forum.

Because this is a preview of future functionality, there is the possibility that it will change, which will possibly
break any existing programs that use this functionality. Because of that, you should never deliver any programs that use
any preview capabilities. For a distributed program, you should wait until it has moved from preview to released state.

## Description

Object that represents an existing CustomFeature feature in a design.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](CustomFeature_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [createForAssemblyContext](CustomFeature_createForAssemblyContext.htm) | Creates or returns a proxy for the native object - i.e. a new object that represents this object but adds the assembly context defined by the input occurrence. |
| [deleteMe](CustomFeature_deleteMe.htm) | Deletes the feature. This works for both parametric and non-parametric features. |
| [dissolve](CustomFeature_dissolve.htm) | Dissolves the feature so that the feature information is lost and only the B-Rep geometry defined by the feature remains. This is only valid for non-parametric features. |
| [setStartAndEndFeatures](CustomFeature_setStartAndEndFeatures.htm) | Sets the start and end features that will be grouped by the custom feature. The "features" in this case can be any object that is visible in the timeline, such as modeling features, sketches, and construction geometry. The input features and all features between them in the timeline will be grouped by the custom feature. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [assemblyContext](CustomFeature_assemblyContext.htm) | Returns the assembly occurrence (i.e. the occurrence) of this object in an assembly. This is only valid in the case where this is acting as a proxy in an assembly. Returns null in the case where the object is not in the context of an assembly but is already the native object. |
| [attributes](CustomFeature_attributes.htm) | Returns the collection of attributes associated with this face. |
| [baseFeature](CustomFeature_baseFeature.htm) | If this feature is associated with a base feature, this property will return that base feature. If it's not associated with a base feature, this property will return null. |
| [bodies](CustomFeature_bodies.htm) | Returns the bodies that were modified or created by this feature. This property works for both parametric and non-parametric features. |
| [customNamedValues](CustomFeature_customNamedValues.htm) | Returns the set of custom named values associated with this custom feature. These are a set of named values that are saved with this feature that you can use to save any additional information that is useful for you in managing the custom feature. For example, you might have a setting like an option for different shapes that the user chooses when creating the feature that are not represented as a parameter. You can use this to save the chosen value so when the feature is computed or edited you can use the value originally chosen. During an edit, you might allow the user to edit this setting and you can update the saved custom value. |
| [definition](CustomFeature_definition.htm) | Gets the CustomFeatureDefinition object associated with this custom feature. null/None is returned in the case where the definition does not exist, which is typically a result of the owning add-in not being loaded. |
| [dependencies](CustomFeature_dependencies.htm) | Returns the collection of dependencies for this custom feature. You can use the collection to query, add, and remove dependencies. |
| [entityToken](CustomFeature_entityToken.htm) | Returns a token for the Feature object. This can be saved and used at a later time with the Design.findEntityByToken method to get back the same feature.   When using entity tokens it's important to understand that the token string returned for a specific entity can be different over time. However, even if you have two different token strings that were obtained from the same entity, when you use findEntityByToken they will both return the same entity. Because of that you should never compare entity tokens as way to determine what the token represents. Instead, you need to use the findEntityByToken method to get the two entities identified by the tokens and then compare them. |
| [errorOrWarningMessage](CustomFeature_errorOrWarningMessage.htm) | Returns the error or warning message in the case where the healthState property returns either WarningFeatureHealthState or ErrorFeatureHealthState. Otherwise this property returns an empty string. |
| [faces](CustomFeature_faces.htm) | Returns the faces that were created by this feature. This works for both parametric and non-parametric features.   Depending on the modifications made to the body after the feature was created, this may not return all of the faces. For example, when a component is created from a body, the original body and its faces no longer exist, so this won't return any faces. However, you can roll the timeline to immediately after the feature, and all the original faces will be available. |
| [features](CustomFeature_features.htm) | Returns the features combined by this custom feature. The start and end features and all of the features between them in the timeline are returned. |
| [healthState](CustomFeature_healthState.htm) | Returns the current health state of the feature. |
| [isParametric](CustomFeature_isParametric.htm) | Indicates if this feature is parametric or not. |
| [isSuppressed](CustomFeature_isSuppressed.htm) | Gets and sets if this feature is suppressed. This is only valid for parametric features. |
| [isValid](CustomFeature_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [linkedFeatures](CustomFeature_linkedFeatures.htm) | Returns the set of features that are linked to this feature. The set of linked features are all of the features that were created in various components as the result of a single feature being created in the user interface. |
| [name](CustomFeature_name.htm) | Returns the name of the feature as seen in the browser (non-parametric) or in the timeline (parametric). |
| [nativeObject](CustomFeature_nativeObject.htm) | The NativeObject is the object outside the context of an assembly and in the context of its parent component. Returns null in the case where this object is not in the context of an assembly but is already the native object. |
| [objectType](CustomFeature_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.   It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType(): |
| [parameters](CustomFeature_parameters.htm) | Returns the list of parameters associated with this custom feature. |
| [parentComponent](CustomFeature_parentComponent.htm) | Returns the parent component that owns this feature. |
| [timelineObject](CustomFeature_timelineObject.htm) | Returns the timeline object associated with this feature. |

## Accessed From

[CustomFeature.createForAssemblyContext](CustomFeature_createForAssemblyContext.htm), [CustomFeature.nativeObject](CustomFeature_nativeObject.htm), [CustomFeatureDependency.parentCustomFeature](CustomFeatureDependency_parentCustomFeature.htm), [CustomFeatureEventArgs.customFeature](CustomFeatureEventArgs_customFeature.htm), [CustomFeatureParameter.parentCustomFeature](CustomFeatureParameter_parentCustomFeature.htm), [CustomFeatures.add](CustomFeatures_add.htm), [CustomFeatures.item](CustomFeatures_item.htm), [CustomFeatures.itemByName](CustomFeatures_itemByName.htm)

## Version

Introduced in version January 2021

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |