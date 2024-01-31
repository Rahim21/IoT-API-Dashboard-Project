from app import *

@app.route("/get_tickets", methods=["GET"])
def get_tickets():
    
    response = requests.get(api_url+"/tickets/")
    
    reference = request.headers.get("Referer")
    
    if response.json().get("statusCode") in [200, 201]:
        flash("Tickets retrieved successfully.", "success")
        return redirect(reference)
    else:
        flash("An error occurred. Please try again later.", "danger")
        return redirect(reference)
    
@app.route("/get_ticket", methods=["POST"])
def get_ticket():
    
    ticket_id = request.form.get("ticket_id")
    
    response = requests.get(api_url+"/tickets/"+ticket_id)
    
    reference = request.headers.get("Referer")
    
    if response.json().get("statusCode") in [200, 201]:
        flash("Ticket retrieved successfully.", "success")
        return redirect(reference)
    else:
        flash("An error occurred. Please try again later.", "danger")
        return redirect(reference)
    
@app.route("/add_ticket", methods=["POST"])
def add_ticket():
    
    name = request.form.get("name")
    ticket_type = request.form.get("ticket_type")
    user_id = session.get("user_id")
    
    data = {"name":name, "ticket_type":ticket_type, "user_id":user_id}
    
    response = requests.post(api_url+"/tickets/add", json=data)
    
    reference = request.headers.get("Referer")
    
    if response.json().get("statusCode") in [200, 201]:
        flash("Ticket added successfully.", "success")
        return redirect(reference)
    else:
        flash("An error occurred. Please try again later.", "danger")
        return redirect(reference)
    
@app.route("/edit_ticket", methods=["POST"])
def edit_ticket():
    
    ticket_id = request.form.get("ticket_id")
    name = request.form.get("name")
    ticket_type = request.form.get("ticket_type")
    
    data = {"name":name, "ticket_type":ticket_type}
    
    response = requests.put(api_url+"/tickets/"+ticket_id+"/edit", json=data)
    
    reference = request.headers.get("Referer")
    
    if response.json().get("statusCode") in [200, 201]:
        flash("Ticket edited successfully.", "success")
        return redirect(reference)
    else:
        flash("An error occurred. Please try again later.", "danger")
        return redirect(reference)
    
@app.route("/delete_ticket", methods=["POST"])
def delete_ticket():
    
    ticket_id = request.form.get("ticket_id")
    
    response = requests.delete(api_url+"/tickets/"+ticket_id+"/delete")
    
    reference = request.headers.get("Referer")
    
    if response.json().get("statusCode") in [200, 201]:
        flash("Ticket deleted successfully.", "success")
        return redirect(reference)
    else:
        flash("An error occurred. Please try again later.", "danger")
        return redirect(reference)