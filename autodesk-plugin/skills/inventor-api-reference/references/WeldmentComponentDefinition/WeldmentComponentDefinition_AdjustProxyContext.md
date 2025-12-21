# WeldmentComponentDefinition.AdjustProxyContext Method

Parent Object: [WeldmentComponentDefinition](../WeldmentComponentDefinition/WeldmentComponentDefinition.md)

## Description

Returns the specified object proxy scoped into this assembly, trimming any portion of the context from any assembly in which this assembly is a subassembly. In other words, for the given object proxy, this method makes a new object proxy which has this component definition as the context definition.

## Syntax

WeldmentComponentDefinition.**AdjustProxyContext**( ***ObjectProxy*** As Object ) As Object

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| ObjectProxy | Object | An object representing an Object Proxy - known in earlier versions of Inventor as a Geom Proxy. Each Object Proxy has an associated ComponentOccurrence, which has a property called ContextDefinition. The value of this property is the top level ComponentDefinition. |

## Version

Introduced in version 8
