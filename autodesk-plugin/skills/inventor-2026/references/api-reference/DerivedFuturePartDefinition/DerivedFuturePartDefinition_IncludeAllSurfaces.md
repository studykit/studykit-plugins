# DerivedFuturePartDefinition.IncludeAllSurfaces Property

Parent Object: [DerivedFuturePartDefinition](../DerivedFuturePartDefinition/DerivedFuturePartDefinition.md)

## Description

Read-write property that defines whether all surfaces are included in the derived part. Valid input for this property is kDerivedIncludeAll, kDerivedExcludeAll, and kDerivedIndividualDefined. If set to kDerivedIncludeAll, all surfaces will be included. If set to kDerivedExcludeAll, no surfaces will be imported. If set to kDerivedIndividualDefined, then the inclusion state of each surface is defined by the surface itself. The available surfaces are accessed using the Surfaces property of the DerivedPartDefinition object.

## Syntax

DerivedFuturePartDefinition.**IncludeAllSurfaces**() As [DerivedComponentOptionEnum](../DerivedComponentOptionEnum.md)

## Property Value

This is a read/write property whose value is a [DerivedComponentOptionEnum](../DerivedComponentOptionEnum.md).

## Version

Introduced in version 2018
