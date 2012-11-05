using System;
using NUnit.Framework;
using mercadopago;
using Newtonsoft.Json;
using Newtonsoft.Json.Linq;

namespace UnitTest {
	
    [TestFixture]
    public class tests {
		MP mp = new MP ("CLIENT_ID", "SECRET_CLIENT");
		
		[Test]
		/* Call preference added through button flow */
        public void getPreference() {
			
            JObject preference = mp.getPreference("ID");
			
            Assert.AreEqual((Int16)preference["status"],200);
			
        }
		
        [Test]
		/* Create a new preference and verify that data result are ok */
        public void createPreference() {
			
            JObject preference = mp.createPreference("{'items':[{'title':'create-dotnet','quantity':1,'currency_id':'ARS','unit_price':10.5}]}");
			
            Assert.AreEqual((Int16)preference["status"],201);
			Assert.AreEqual((String)preference["response"]["items"][0]["title"],"create-dotnet");
			
        }
		
		
		[Test]
		/* We create a new preference, we modify this one and then we verify that data are ok. */
        public void updatePreference() {
			
            JObject preferenceCreated = mp.createPreference("{'items':[{'title':'create-dotnet','quantity':1,'currency_id':'ARS','unit_price':10.5}]}");
			
			JObject preferenceUpdate = mp.updatePreference((String)preferenceCreated["response"]["id"], "{'items':[{'title':'update-dotnet','quantity':1,'currency_id':'ARS','unit_price':10.5}]}");
			Assert.AreEqual((Int16)preferenceUpdate["status"],200);
			
			JObject preferenceUpdated = mp.getPreference((String)preferenceCreated["response"]["id"]);
			Assert.AreEqual((String)preferenceUpdated["response"]["items"][0]["title"],"update-dotnet");
			
        }
    }
	
}