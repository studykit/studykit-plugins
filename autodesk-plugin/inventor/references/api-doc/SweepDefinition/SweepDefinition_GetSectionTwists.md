# SweepDefinition.GetSectionTwists Method

Parent Object: [SweepDefinition](../SweepDefinition/SweepDefinition.md)

## Description

Method that gets the twisted sweep sections and the twist conditions at these sections. This method is applicable when the SweepType is kPathAndSectionTwistSweepType.

## Remarks

This method returns the sweep path points at which section twists have been specified in the SectionTwistPoints object collection and the corresponding twists for these sweep sections in the SectionTwistVectors object collection. If no twist conditions have been specified for any of the sweep sections, then both the arguments will return Nothing.

## Syntax

SweepDefinition.**GetSectionTwists**( ***SectionTwistPoints*** As [ObjectCollection](../ObjectCollection/ObjectCollection.md), ***SectionTwistVectors*** As [ObjectCollection](../ObjectCollection/ObjectCollection.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| SectionTwistPoints | [ObjectCollection](../ObjectCollection/ObjectCollection.md) | Output ObjectCollection that contains the points along the sweep path at which the sweep twists have been specified. The sweep path points define the positions of the sweep cross-sections at which the twists have been specified. Since the sweep feature is created by sweeping a profile cross-section along a sweep path, the twist of the sweep can theoretically be controlled at all points along the sweep path. But for practical purposes, the creation of a twisted sweep feature is limited to sweep features that are swept along a spline path and the twist can only be specified for cross-sections at fit points of the spline path. Since the sweep feature can only be twisted at fit points of the spline that defines the sweep path, the objects returned in the collection will correspond to those fit points at which the twists have been specified. The objects returned in the collection will be either SketchPoint objects that correspond to one of the fit points of the sweep path if it is a 2D spline or SketchPoint3D objects that correspond to one of the fit points of the sweep path if it is a 3D spline. Since this argument together with the SectionTwistVectors argument defines the twist conditions at the cross-sections of the sweep at which the twists have been specified, the order of the sweep path points in the collection returned by this argument will correspond to the order of the twist unit-vectors in the collection returned by the SectionTwistVectors argument. Therefore, if a particular item number in the collection returned by this argument corresponds to a particular sweep path point at which the sweep section has been twisted, the same item number in the collection returned by the SectionTwistVectors argument will correspond to the twist vector for that sweep section. For example, if a twist condition has been applied for the sweep cross-section at the first fit point of the sweep path and if the first item in the collection returned by this argument is the first fit point of the sweep path, then the first item in the collection returned by the SectionTwistVectors argument will be the twist vector for the cross-section at the first fit point of the sweep path. If no twist conditions have been specified for any of the sweep sections, then this argument will return Nothing. |
| SectionTwistVectors | [ObjectCollection](../ObjectCollection/ObjectCollection.md) | Output ObjectCollection object that contains the unit-vectors that define the twists for the sweep sections. The sweep twist vectors define the twists for the sweep cross-sections returned in the SectionTwistPoints argument. The twist vectors are unit-vectors specified in the model space coordinate system. Also, each vector lies on the plane of the sweep cross-section for which it defines the twist. The objects returned in the collection will be UnitVector objects that specify the twist vector directions for the sweep sections. Since this argument together with the SectionTwistPoints argument defines the twist conditions at the cross-sections of the sweep at which the twists have been specified, the order of the twist unit-vectors in the collection returned by this argument will correspond to the order of the sweep path points in the collection returned by the SectionTwistPoints argument. Therefore, if a particular item number in the collection returned by the SectionTwistPoints argument corresponds to a particular sweep path point at which the sweep section has been twisted, the same item number in the collection returned by this argument will correspond to the twist vector for that sweep section. For example, if a twist condition has been applied for the sweep cross-section at the first fit point of the sweep path and if the first item in the collection returned by the SectionTwistPoints argument is the first fit point of the sweep path, then the first item in the collection returned by this argument will be the twist vector for the cross-section at the first fit point of the sweep path. |

## Version

Introduced in version 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |